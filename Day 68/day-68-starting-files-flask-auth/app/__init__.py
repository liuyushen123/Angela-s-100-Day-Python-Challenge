from flask import Flask

from config import Config
from app.extensions import db, login_manager
from app.controllers import blueprints


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    with app.app_context():
        db.create_all()

    return app
