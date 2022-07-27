from develop import develop_blueprint
from werkzeug.routing import BaseConverter


@develop_blueprint.route(rule='/')
def develop_root():
    return 'develop home page'

