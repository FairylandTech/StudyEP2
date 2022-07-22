from release import release_blueprint
from werkzeug.routing import BaseConverter

@release_blueprint.route(rule='/root')
def release_root():
    return 'Hello'


@release_blueprint.route(rule='/<string:user>/index')
def release_index(user: str):
    try:
        data = f'Hello {user} !'
        return data
    except Exception as error:
        print(error)