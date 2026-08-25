import os
import re
import uuid
from functools import wraps

from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.utils import secure_filename

from config import Config
from models.database import Admin, Download, SupportTicket, Template, db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_id"):
            flash("لطفاً ابتدا وارد شوید.", "warning")
            return redirect(url_for("admin.login"))
        return f(*args, **kwargs)

    return decorated


def superadmin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_id"):
            return redirect(url_for("admin.login"))
        admin = Admin.query.get(session["admin_id"])
        if not admin or not admin.is_superadmin:
            flash("دسترسی غیرمجاز.", "error")
            return redirect(url_for("admin.dashboard"))
        return f(*args, **kwargs)

    return decorated


def allowed_file(filename, allowed):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"[^\w\-]+", "", text, flags=re.UNICODE)
    return text or str(uuid.uuid4())[:8]


def save_upload(file, folder, allowed):
    if not file or file.filename == "":
        return None
    if not allowed_file(file.filename, allowed):
        return None
    ext = file.filename.rsplit(".", 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{ext}"
    path = os.path.join(folder, filename)
    file.save(path)
    return filename


def delete_file(folder, filename):
    if filename:
        path = os.path.join(folder, filename)
        if os.path.exists(path):
            os.remove(path)


@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("admin_id"):
        return redirect(url_for("admin.dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            session["admin_id"] = admin.id
            session["admin_name"] = admin.full_name
            session["is_superadmin"] = admin.is_superadmin
            from datetime import datetime, timezone

            admin.last_login = datetime.now(timezone.utc)
            db.session.commit()
            flash("خوش آمدید!", "success")
            return redirect(url_for("admin.dashboard"))
        flash("نام کاربری یا رمز عبور اشتباه است.", "error")

    return render_template("admin/login.html")


@admin_bp.route("/logout")
def logout():
    session.clear()
    flash("با موفقیت خارج شدید.", "success")
    return redirect(url_for("admin.login"))


@admin_bp.route("/")
@admin_bp.route("/dashboard")
@login_required
def dashboard():
    total_templates = Template.query.count()
    total_downloads = Download.query.count()
    total_tickets = SupportTicket.query.filter_by(is_read=False).count()
    recent_downloads = Download.query.order_by(Download.downloaded_at.desc()).limit(10).all()
    popular_templates = Template.query.order_by(Template.download_count.desc()).limit(5).all()
    return render_template(
        "admin/dashboard.html",
        total_templates=total_templates,
        total_downloads=total_downloads,
        total_tickets=total_tickets,
        recent_downloads=recent_downloads,
        popular_templates=popular_templates,
    )


@admin_bp.route("/templates")
@login_required
def templates_list():
    templates = Template.query.order_by(Template.created_at.desc()).all()
    return render_template("admin/templates.html", templates=templates)


@admin_bp.route("/templates/add", methods=["POST"])
@login_required
def template_add():
    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    short_description = request.form.get("short_description", "").strip()
    category = request.form.get("category", "عمومی").strip()
    tags = request.form.get("tags", "").strip()
    is_featured = request.form.get("is_featured") == "on"
    meta_title = request.form.get("meta_title", "").strip()
    meta_description = request.form.get("meta_description", "").strip()
    meta_keywords = request.form.get("meta_keywords", "").strip()

    image = request.files.get("image")
    zip_file = request.files.get("zip_file")

    if not name or not description:
        flash("نام و توضیحات الزامی است.", "error")
        return redirect(url_for("admin.templates_list"))

    image_filename = save_upload(image, Config.IMAGE_UPLOAD_FOLDER, Config.ALLOWED_IMAGE_EXTENSIONS)
    zip_filename = save_upload(zip_file, Config.TEMPLATE_UPLOAD_FOLDER, Config.ALLOWED_ZIP_EXTENSIONS)

    if not image_filename or not zip_filename:
        delete_file(Config.IMAGE_UPLOAD_FOLDER, image_filename)
        delete_file(Config.TEMPLATE_UPLOAD_FOLDER, zip_filename)
        flash("فایل تصویر و ZIP الزامی است.", "error")
        return redirect(url_for("admin.templates_list"))

    slug = slugify(name)
    existing = Template.query.filter_by(slug=slug).first()
    if existing:
        slug = f"{slug}-{uuid.uuid4().hex[:6]}"

    template = Template(
        name=name,
        slug=slug,
        description=description,
        short_description=short_description or description[:300],
        category=category,
        tags=tags,
        image_filename=image_filename,
        zip_filename=zip_filename,
        is_featured=is_featured,
        meta_title=meta_title or name,
        meta_description=meta_description or short_description,
        meta_keywords=meta_keywords,
    )
    db.session.add(template)
    db.session.commit()
    flash("قالب با موفقیت اضافه شد.", "success")
    return redirect(url_for("admin.templates_list"))


@admin_bp.route("/templates/<int:template_id>/edit", methods=["POST"])
@login_required
def template_edit(template_id):
    template = Template.query.get_or_404(template_id)
    template.name = request.form.get("name", template.name).strip()
    template.description = request.form.get("description", template.description).strip()
    template.short_description = request.form.get("short_description", "").strip()
    template.category = request.form.get("category", template.category).strip()
    template.tags = request.form.get("tags", "").strip()
    template.is_featured = request.form.get("is_featured") == "on"
    template.is_active = request.form.get("is_active") == "on"
    template.meta_title = request.form.get("meta_title", "").strip()
    template.meta_description = request.form.get("meta_description", "").strip()
    template.meta_keywords = request.form.get("meta_keywords", "").strip()

    image = request.files.get("image")
    zip_file = request.files.get("zip_file")

    if image and image.filename:
        new_image = save_upload(image, Config.IMAGE_UPLOAD_FOLDER, Config.ALLOWED_IMAGE_EXTENSIONS)
        if new_image:
            delete_file(Config.IMAGE_UPLOAD_FOLDER, template.image_filename)
            template.image_filename = new_image

    if zip_file and zip_file.filename:
        new_zip = save_upload(zip_file, Config.TEMPLATE_UPLOAD_FOLDER, Config.ALLOWED_ZIP_EXTENSIONS)
        if new_zip:
            delete_file(Config.TEMPLATE_UPLOAD_FOLDER, template.zip_filename)
            template.zip_filename = new_zip

    db.session.commit()
    flash("قالب با موفقیت ویرایش شد.", "success")
    return redirect(url_for("admin.templates_list"))


@admin_bp.route("/templates/<int:template_id>/delete", methods=["POST"])
@login_required
def template_delete(template_id):
    template = Template.query.get_or_404(template_id)
    delete_file(Config.IMAGE_UPLOAD_FOLDER, template.image_filename)
    delete_file(Config.TEMPLATE_UPLOAD_FOLDER, template.zip_filename)
    db.session.delete(template)
    db.session.commit()
    flash("قالب حذف شد.", "success")
    return redirect(url_for("admin.templates_list"))


@admin_bp.route("/downloads")
@login_required
def downloads_list():
    downloads = Download.query.order_by(Download.downloaded_at.desc()).all()
    return render_template("admin/downloads.html", downloads=downloads)

@admin_bp.route("/admins")
@superadmin_required
def admins_list():
    admins = Admin.query.order_by(Admin.created_at.desc()).all()
    return render_template("admin/admins.html", admins=admins)


@admin_bp.route("/admins/add", methods=["POST"])
@superadmin_required
def admin_add():
    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip()
    full_name = request.form.get("full_name", "").strip()
    password = request.form.get("password", "")
    is_superadmin = request.form.get("is_superadmin") == "on"

    if not all([username, email, full_name, password]):
        flash("همه فیلدها الزامی است.", "error")
        return redirect(url_for("admin.admins_list"))

    if Admin.query.filter((Admin.username == username) | (Admin.email == email)).first():
        flash("نام کاربری یا ایمیل تکراری است.", "error")
        return redirect(url_for("admin.admins_list"))

    admin = Admin(username=username, email=email, full_name=full_name, is_superadmin=is_superadmin)
    admin.set_password(password)
    db.session.add(admin)
    db.session.commit()
    flash("ادمین جدید اضافه شد.", "success")
    return redirect(url_for("admin.admins_list"))


@admin_bp.route("/admins/<int:admin_id>/delete", methods=["POST"])
@superadmin_required
def admin_delete(admin_id):
    if admin_id == session.get("admin_id"):
        flash("نمی‌توانید خودتان را حذف کنید.", "error")
        return redirect(url_for("admin.admins_list"))
    admin = Admin.query.get_or_404(admin_id)
    db.session.delete(admin)
    db.session.commit()
    flash("ادمین حذف شد.", "success")
    return redirect(url_for("admin.admins_list"))
