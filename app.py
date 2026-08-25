import os
from flask import Flask, session
from config import Config
from models.database import init_db
from routes.admin import admin_bp
from routes.public import public_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(Config.TEMPLATE_UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(Config.IMAGE_UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(os.path.join(app.root_path, "instance"), exist_ok=True)

    init_db(app)

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)

    @app.context_processor
    def inject_globals():
        return {
            "site_name": Config.SITE_NAME,
            "site_url": Config.SITE_URL,
            "support_phone": Config.SUPPORT_PHONE,
            "support_email": Config.SUPPORT_EMAIL,
            "developer_email": Config.DEVELOPER_EMAIL,
            "support_address": Config.SUPPORT_ADDRESS,
        }

    @app.errorhandler(404)
    def not_found(e):
        from flask import render_template
        return render_template("404.html"), 404
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5500)
