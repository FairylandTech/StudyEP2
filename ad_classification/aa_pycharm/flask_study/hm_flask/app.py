from flask import Flask
from config import app_config

# 配置文件的加载
# 1. 配置对象中加载
# class DefaultConfig(object):
#     MYSQL_URL = 'mysql address'
#     REDIS_URL = 'redis address'
# 2. 配置文件中加载

# 创建flask的实例对象
# __name__ 的所用是确定程序启动文件所在的位置;
app = Flask(__name__)
# 获取配置对象中加载
app.config.from_object(app_config.DefaultConfig)
# 获取配置文件中加载
app.config.from_pyfile(filename='./config/settings.py')
app.config.from_pyfile(filename='./config/settings.ini')
# 环境变量配置中加载
# //


# 定义路由和视图函数
@app.route('/')
def hello_world():
    # 实例对象加载
    print(app.config.get('MYSQL_URL'))
    print(app.config.get('REDIS_URL'))
    # 配置文件加载
    print(app.config.get('SESSION'))
    print(app.config.get('TOKEN'))
    # 环境变量加载
    # //
    return 'Hello World!'


# 程序入口
## 当文件独立运行时, 表达式成立
## 当文件被导入到其他文件中调用, 该表达式不成立, __name__ == app  # app: 文件名
if __name__ == '__main__':
    app.run()
