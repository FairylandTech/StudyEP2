# 基础模块
from flask import Flask
import factory_module
from config import app_config
# 转换器
from werkzeug.routing import BaseConverter
# 蓝图模块
from flask import Blueprint
import users
from users import views
import testing
from testing import views

## 配置文件的加载
### 配置对象中加载
# class DefaultConfig(object):
#     MYSQL_URL = 'mysql address'
#     REDIS_URL = 'redis address'

## 创建flask的实例对象
## __name__ 的所用是确定程序启动文件所在的位置;
# app = Flask(__name__)

## 配置文件的加载
### 获取配置对象中加载
# app.config.from_object(app_config.DefaultConfig)
# 获取配置文件中加载
# app.config.from_pyfile(filename='./config/settings.py')
# app.config.from_pyfile(filename='./config/settings.ini')
# 环境变量配置中加载
# //

# 工厂模式: 
# 1. 定义工厂函数, 封装创建程序的实例
# 2. 定义工厂函数的参数, 可以根据函数的不同, 生成不同的app
study_app = factory_module.FactoryModules.create_study(app_config.DefaultConfig)

##　蓝图
### 蓝图对象
bp = Blueprint(name='bp', import_name=__name__, url_prefix='/root/')


# 定义路由和视图函数
@study_app.route('/', methods=['GET'])
def root():
    # 实例对象加载
    # print(study_app.config.get('MYSQL_URL'))
    # print(study_app.config.get('REDIS_URL'))
    # 配置文件加载
    # print(study_app.config.get('SESSION'))
    # print(study_app.config.get('TOKEN'))
    # 环境变量加载
    # //
    return 'Home Page'


## 蓝图路由
@bp.route(rule='/user')
def get_user():
    return 'User Info'


## 注册蓝图
# study_app.register_blueprint(blueprint=bp)
### 用户 
# study_app.register_blueprint(blueprint=users.users_bp)
### 测试
study_app.register_blueprint(blueprint=testing.test_api)

## 程序入口
### 当文件独立运行时, 表达式成立
### 当文件被导入到其他文件中调用, 该表达式不成立, __name__ == app  # app: 文件名
## run方法:
## debug=True, 开启debug模式可以自动跟踪代码的变化, 定位错误信息
## host/post host可以指定主机地址, post可以指定服务端口, 
if __name__ == '__main__':
    print(study_app.url_map)
    study_app.run(debug=True, host='0.0.0.0', port=8001)
