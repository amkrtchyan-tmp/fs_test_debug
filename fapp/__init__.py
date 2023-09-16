import os
from datetime import datetime

from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore, hash_password
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

from fapp.config import app_config

APP_CONF = os.getenv('APP_CONF') or 'default'

db: SQLAlchemy = SQLAlchemy()
security: Security = Security()


def init_db():
    db.drop_all()
    db.create_all()
    security.datastore.find_or_create_role(name='admin', description='Admin role')
    db.session.commit()
    admin_user = dict(email='admin@domain.com', password=hash_password('123'),
                      confirmed_at=datetime.utcnow(), roles=['admin'])
    security.datastore.create_user(**admin_user)
    db.session.commit()


def create_app(config_name: str) -> Flask:
    print(f"App config {APP_CONF}")
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)

    from fapp.auth.models import User, Role
    security.init_app(app, datastore=SQLAlchemyUserDatastore(db, User, Role))

    from fapp.auth import auth
    app.register_blueprint(auth)
    from fapp.main import main
    app.register_blueprint(main)

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

    with app.app_context():
        init_db()

    return app


app = create_app(APP_CONF)
