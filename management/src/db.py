from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

import os

db_instance = SQLAlchemy()

POSTGRES_DSN = f'postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('DEFAULT_DB_NAME')}'

def config_sql_alchemy(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_DSN
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO')
    db_instance.app = app
    db_instance.init_app(app)


def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            db_instance.session.commit()
            return True
        except SQLAlchemyError:
            db_instance.session.rollback()
            return False
    return persist