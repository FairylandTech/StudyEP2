# 基础模块
from flask import Flask
# 配置
from config.develop.config import DevelopmentConfig
# 蓝图
from develop import develop_blueprint
from develop import views
# 工厂
from factory_module.develop.factory_develop_module import FactoryModules


# 工厂
develop_app = FactoryModules.create_app_develop(config_name=DevelopmentConfig)
# 蓝图注册
develop_app.register_blueprint(blueprint=develop_blueprint)


if __name__ == '__main__':
    develop_app.run(debug=True, host='0.0.0.0', port=8001)
