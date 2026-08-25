import os
import uuid

from flask import (
    Blueprint,
    abort,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from config import Config
from models.database import Download, SupportTicket, Template, db

public_bp = Blueprint("public", __name__)


@public_bp.route("/")
def index():
    featured = Template.query.filter_by(is_active=True, is_featured=True).limit(6).all()
    latest = Template.query.filter_by(is_active=True).order_by(Template.created_at.desc()).limit(6).all()
    total_templates = Template.query.filter_by(is_active=True).count()
    total_downloads = db.session.query(db.func.sum(Template.download_count)).scalar() or 0
    return render_template(
        "index.html",
        featured=featured,
        latest=latest,
        total_templates=total_templates,
        total_downloads=total_downloads,
    )


@public_bp.route("/templates")
def templates_page():
    category = request.args.get("category", "")
    search = request.args.get("q", "").strip()
    query = Template.query.filter_by(is_active=True)

    if category:
        query = query.filter_by(category=category)
    if search:
        query = query.filter(
            db.or_(
                Template.name.contains(search),
                Template.description.contains(search),
                Template.tags.contains(search),
            )
        )

    templates = query.order_by(Template.created_at.desc()).all()
    categories = (
        db.session.query(Template.category)
        .filter_by(is_active=True)
        .distinct()
        .all()
    )
    categories = [c[0] for c in categories]
    return render_template(
        "templates.html",
        templates=templates,
        categories=categories,
        current_category=category,
        search=search,
    )


@public_bp.route("/templates/<slug>")
def template_detail(slug):
    template = Template.query.filter_by(slug=slug, is_active=True).first_or_404()
    related = (
        Template.query.filter(
            Template.category == template.category,
            Template.id != template.id,
            Template.is_active == True,
        )
        .limit(4)
        .all()
    )
    return render_template("template_detail.html", template=template, related=related)


@public_bp.route("/download/<slug>")
def download_template(slug):
    template = Template.query.filter_by(slug=slug, is_active=True).first_or_404()
    zip_path = os.path.join(Config.TEMPLATE_UPLOAD_FOLDER, template.zip_filename)
    if not os.path.exists(zip_path):
        abort(404)

    download = Download(
        template_id=template.id,
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent", "")[:300],
    )
    template.download_count += 1
    db.session.add(download)
    db.session.commit()

    return send_from_directory(
        Config.TEMPLATE_UPLOAD_FOLDER,
        template.zip_filename,
        as_attachment=True,
        download_name=f"{template.slug}.zip",
    )


@public_bp.route("/support", methods=["GET", "POST"])
def support():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not all([name, email, subject, message]):
            flash("لطفاً فیلدهای الزامی را پر کنید.", "error")
        else:
            ticket = SupportTicket(name=name, email=email, phone=phone, subject=subject, message=message)
            db.session.add(ticket)
            db.session.commit()
            flash("تیکت شما با موفقیت ثبت شد. به زودی پاسخ می‌دهیم.", "success")
            return redirect(url_for("public.support"))

    return render_template("support.html")


@public_bp.route("/about")
def about():
    return render_template("about.html")


@public_bp.route("/robots.txt")
def robots():
    return (
        "User-agent: *\nAllow: /\nDisallow: /admin/\nSitemap: "
        + Config.SITE_URL
        + "/sitemap.xml\n",
        200,
        {"Content-Type": "text/plain"},
    )


@public_bp.route("/sitemap.xml")
def sitemap():
    templates = Template.query.filter_by(is_active=True).all()
    pages = [
        {"loc": "/", "priority": "1.0"},
        {"loc": "/templates", "priority": "0.9"},
        {"loc": "/support", "priority": "0.7"},
        {"loc": "/about", "priority": "0.7"},
    ]
    for t in templates:
        pages.append({"loc": f"/templates/{t.slug}", "priority": "0.8"})

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        xml += "  <url>\n"
        xml += f"    <loc>{Config.SITE_URL}{page['loc']}</loc>\n"
        xml += f"    <priority>{page['priority']}</priority>\n"
        xml += "  </url>\n"
    xml += "</urlset>"
    return xml, 200, {"Content-Type": "application/xml"}
