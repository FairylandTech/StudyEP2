from flask import Blueprint

test_api = Blueprint(name='test_api', import_name=__name__, url_prefix='/test')

