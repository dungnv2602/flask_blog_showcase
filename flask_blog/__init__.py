from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.login_message = u"Please login before doing anything."
login_manager.refresh_view = "users.login"
login_manager.needs_refresh_message_category = "info"
login_manager.needs_refresh_message = u"To protect your account, please reauthenticate to access this page."


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or
        'sqlite:///' + os.path.join(app.instance_path, 'site.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        REMEMBER_COOKIE_DURATION=timedelta(hours=48),
        # REMEMBER_COOKIE_SECURE = HTTPS
        MAIL_SERVER='smtp.googlemail.com',
        MAIL_POST=587,
        MAIL_USE_TLS=True,
        MAIL_DEFAULT_SENDER='yourId@gmail.com',
        MAIL_USERNAME=os.environ.get('EMAIL_USERNAME'),
        MAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')
    )

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flask_blog.users.routes import users
    from flask_blog.posts.routes import posts
    from flask_blog.main.routes import main
    from flask_blog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
