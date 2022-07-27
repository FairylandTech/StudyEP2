from flask import Blueprint

beta_blueprint = Blueprint(name='beta_blueprint', import_name=__name__, url_prefix='/beta')