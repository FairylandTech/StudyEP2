from flask import Blueprint

users_bp = Blueprint(name='users_bp', import_name=__name__, url_prefix='/user')