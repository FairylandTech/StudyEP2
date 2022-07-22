# 基础模块
from flask import Flask
# 配置
from config.beta.config import BetaConfig
# 蓝图
from beta import beta_blueprint
from beta import views
# 工厂
from factory_module.beta.factory_beta_module import FactoryModules


# 工厂
beta_app = FactoryModules.create_app_beta(config_name=BetaConfig)
# 蓝图注册
beta_app.register_blueprint(blueprint=beta_blueprint)


if __name__ == '__main__':
    beta_app.run(debug=True, host='0.0.0.0', port=8001)
