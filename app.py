from flask import Flask
from auth import login_manager
from config import config
from flask_sqlalchemy import SQLAlchemy
from src.DAL.db import db
from src.API.Publications import publications_rout
from src.API.Users import users_rout
from flasgger import Swagger

app = Flask(__name__)


def page_not_fount():
    return '<h1>error...<h1>', 404


@app.route('/')
def hello():
    return '<h1>prueba de desarrollo python</h1>'


if __name__ == '__main__':
    app.config.from_object(config['develoment'])
    app.register_blueprint(publications_rout, url_prefix='/api/publications')
    app.register_blueprint(users_rout, url_prefix='/api/users')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/pruebadb'
    SQLAlchemy(app)
    with app.app_context():
        db.create_all()
    login_manager.init_app(app)
    swagger = Swagger(app)
    app.register_error_handler(404, page_not_fount())
    app.run()
