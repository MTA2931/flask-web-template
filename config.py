import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "website-flask-dev-secret-change-in-production")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'instance' / 'bifront.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
    TEMPLATE_UPLOAD_FOLDER = UPLOAD_FOLDER / "templates"
    IMAGE_UPLOAD_FOLDER = UPLOAD_FOLDER / "images"
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
    ALLOWED_ZIP_EXTENSIONS = {"zip"}
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "gif"}
    SITE_NAME = "نام وبسایت"
    SITE_URL = os.environ.get("SITE_URL", "http://localhost:5000")
    SUPPORT_PHONE = "0915-000-000"
    SUPPORT_EMAIL = "support@domain.com"
    DEVELOPER_EMAIL = "developer@domain.com"
    SUPPORT_ADDRESS = ""
