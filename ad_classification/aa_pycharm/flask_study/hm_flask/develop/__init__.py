from flask import Blueprint

develop_blueprint = Blueprint(name='release_blueprint', import_name=__name__, url_prefix='/develop')