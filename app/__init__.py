"""

AUTOR: Maria Jose Simón

FECHA DE CREACIÓN: 04 octubre 2024

"""

from flask import Flask
from flask import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://robot:farmae@EPJRUIZ\\SQLEXPRESS\\/Mi_PWinR?driver=ODBC+Driver+17+for+SQL+Server"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    login_manager.login_view = "login"

    db.init_app(app)

    # Registro de los Blueprints
    from .users import users_bp
    app.register_blueprint(users_bp)

    from .admins import admins_bp
    app.register_blueprint(admins_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    return app