# coding=utf-8
# 基础模块
from flask import Flask
# 配置
from config.develop.config import DevelopmentConfig
# 蓝图
from develop import develop_blueprint
from develop import views
# 工厂
from factory_module.develop.factory_develop_module import FactoryModules
# 转换器
from werkzeug.routing import BaseConverter
# 用户信息验证
from flask import g, request, current_app, session, render_template, abort

# 工厂
develop_app = FactoryModules.create_app_develop(config_name=DevelopmentConfig)
# 蓝图注册
develop_app.register_blueprint(blueprint=develop_blueprint)


# 转换器
class Telephone(BaseConverter):
    regex = '1[3-9]\d{9}'


develop_app.url_map.converters['telephone'] = Telephone


# 用户登录验证
def auto_login(func):
    def wrapper(*args, **kwargs):
        if g.user_name is not None:
            return func(*args, **kwargs)
        else:
            return abort(401)

    return wrapper


@develop_app.route('/')
def home_page():
    return 'Home Page'


@develop_app.route('/profile')
@auto_login
def profile_home():
    return f'Welcome {g.user_name}'


@develop_app.before_request
def auto_user():
    # g.user_name = 'Alice'
    g.user_name = None


@develop_app.errorhandler(401)
def auto_error(error):
    return render_template('401.html')


if __name__ == '__main__':
    print(develop_app.url_map)
    develop_app.run(debug=True, host='0.0.0.0', port=8001)
