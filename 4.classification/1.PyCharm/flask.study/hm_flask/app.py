from flask import Flask

# 配置文件的加载
# 1. 配置对象中加载
class DefaultConfig(object):
    MYSQL_URL = 'mysql address'

# 创建flask的实例对象
# __name__ 的所用是确定程序启动文件所在的位置;
app = Flask(__name__)
# 获取配置信息
app.config.from_object(DefaultConfig)


# 定义路由和视图函数
@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!'


# 程序入口
## 当文件独立运行时, 表达式成立
## 当文件被导入到其他文件中调用, 该表达式不成立, __name__ == app  # app: 文件名
if __name__ == '__main__':
    app.run()
