# 基础模块
from flask import Flask
# 工厂模型
from factory_module.release.factory_release_module import FactoryModules
# 配置文件
from config.release.config import DefaultConfig, DevelopmentConfig, ProductionConfig
# 转换器
from werkzeug.routing import BaseConverter
# 蓝图模块
from release import release_blueprint
from release import root_blueprint
from release import views



# 工厂初始化
release_app = FactoryModules.create_app_release(config_name=DefaultConfig)
# 注册蓝图
release_app.register_blueprint(blueprint=release_blueprint)
release_app.register_blueprint(blueprint=root_blueprint)


if __name__ == '__main__':
    release_app.run(debug=True, host='0.0.0.0', port=8001)
