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


# 工厂
develop_app = FactoryModules.create_app_develop(config_name=DevelopmentConfig)
# 蓝图注册
develop_app.register_blueprint(blueprint=develop_blueprint)


# 转换器
class Telephone(BaseConverter):
    regex = r'1[3-9]\d{9}'


develop_app.url_map.converters['telephone'] = Telephone


@develop_app.route(rule='/root/<telephone:number>')
def root_tel(number):
    data = f'电话: {number}'
    return data


@develop_blueprint.route(rule='/<int:number>')
def develop_telephone(number):
    data = f'手机号码{number}'
    return data


if __name__ == '__main__':
    develop_app.run(debug=True, host='0.0.0.0', port=8001)
