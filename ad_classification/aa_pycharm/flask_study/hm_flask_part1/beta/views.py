from beta import beta_blueprint
from werkzeug.routing import BaseConverter

@beta_blueprint.route(rule='/root/')
def develop_root():
    return 'beta home page'


@beta_blueprint.route(rule='/<int:number>')
def develop_telephone(number):
    data = f'手机号码{number}'
    return data
