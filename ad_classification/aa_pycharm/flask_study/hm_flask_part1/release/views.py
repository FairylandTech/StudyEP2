from release import release_blueprint
from release import root_blueprint
from werkzeug.routing import BaseConverter
from flask import redirect

@release_blueprint.route(rule='/root')
def release_root():
    return 'Hello'


@release_blueprint.route(rule='/<string:user>/index')
def release_index(user: str):
    try:
        data = f'Hello {user} !'
        return data
    except Exception as error:
        data = error
        return data
    
    
@root_blueprint.route(rule='/')
def path_root():
    try:
        data = 'Home Page'
        return redirect(location='https://github.com/AliceEngineerPro')
    except Exception as error:
        data = error
        return data
    
    