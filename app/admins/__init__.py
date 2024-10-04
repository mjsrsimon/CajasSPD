from flask import Blueprint

admins_bp = Blueprint('admins', __name__, template_folder='templates')

from . import routes