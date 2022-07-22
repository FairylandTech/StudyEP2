from develop import develop_blueprint
from werkzeug.routing import BaseConverter

@develop_blueprint.route(rule='/root/')
def develop_root():
    return 'develop home page'


@develop_blueprint.route(rule='/<int:number>')
def develop_telephone(number):
    data = f'手机号码{number}'
    return data
