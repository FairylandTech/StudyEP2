# encoding=utf-8
# 基础模块
from flask import Flask
from factory_module.factory_moduls import FactoryModules
from config import app_config
# 转换器 (url匹配)
from werkzeug.routing import BaseConverter
# 蓝图模块 (自定义)
from flask import Blueprint
from users import users_bp
from users import views
from testing import test_api
from testing import views
# request 模块
from flask import request
# 项目根路径
from public.path_file.root_path import ROOT_PATH
# flask 模板文件
from flask import render_template
# 重定向url
from flask import redirect
# json 模块
from flask import jsonify
import json
# cookie 模块
from flask import make_response
# session 模块
from flask import session
# 异常处理 abort
from flask import abort
# g 对象
from flask import g, current_app

# 配置文件的加载
# 配置对象中加载
# class DefaultConfig(object):
#     MYSQL_URL = 'mysql address'
#     REDIS_URL = 'redis address'

# 创建flask的实例对象
# __name__ 的所用是确定程序启动文件所在的位置;
# app = Flask(__name__)

# 配置文件的加载
# 获取配置对象中加载
# app.config.from_object(app_config.DefaultConfig)
# 获取配置文件中加载
# app.config.from_pyfile(filename='./config/settings.py')
# app.config.from_pyfile(filename='./config/settings.ini')
# 环境变量配置中加载
# #

# 工厂模式: 
# 1. 定义工厂函数, 封装创建程序的实例
# 2. 定义工厂函数的参数, 可以根据函数的不同, 生成不同的app
study_app = FactoryModules.create_study(config_name=app_config.DefaultConfig)

# 　蓝图
# 蓝图对象
bp = Blueprint(name='bp', import_name=__name__, url_prefix='/root/')


# 定义路由和视图函数
@study_app.route('/root', methods=['GET'])
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


# 蓝图路由
@bp.route(rule='/user')
def get_user():
    return 'User Info'


# 注册蓝图
# study_app.register_blueprint(blueprint=bp)
# 用户 
# study_app.register_blueprint(blueprint=users.users_bp)
# 测试
study_app.register_blueprint(blueprint=test_api)


# 转换器
class Telephone(BaseConverter):
    regex = r'1[3-9]\d{9}'


study_app.url_map.converters['telephone'] = Telephone


@study_app.route(rule='/root/<telephone:number>')
def root_tel(number):
    data = f'电话: {number}'
    return data


# request 对象
@study_app.route(rule='/', methods=['GET', 'POST'])
def index():
    # 字符串查询
    # str_data = request.args.get('str_data')
    # str_result_data = 'TEL: {}'.format(str_data)
    # return str_result_data

    # form 表单查询
    form_data_user = request.form.get('user')
    form_data_passwd = request.form.get('passwd')
    # print(f'user={form_data_user}, passwd={form_data_passwd}')
    # print(request.headers)
    return 'Hello'


@study_app.route(rule='/uploads/images', methods=['POST'])
def save_images():
    image = request.files.get('image')
    print(f'image={image}')
    file_dir = f'{ROOT_PATH}static/images/1.jpg'
    image.save(file_dir)
    return 'Save Images Successfully'


@study_app.route('/templates_index')
def templates_index():
    return render_template('notes/index.html')


@study_app.route('/json/index')
def json_index():
    data = {"json": 12}
    # 内置函数
    return jsonify(data)
    # json 模块
    # data = json.dumps(data)
    # return data


# cookie操作: 创建和获取
# 创建
@study_app.route(rule='/cookie')
def make_cookie():
    data_cookie = make_response('set cookie info')
    # 
    data_cookie.set_cookie('K', 'V', max_age=600)
    return data_cookie


# 获取
@study_app.route(rule='/cookie_get')
def get_cookie():
    get_cookie = request.cookies.get('K')
    return get_cookie


# session 创建
@study_app.route(rule='/session')
def make_session():
    session['K'] = 'V'
    return redirect(location='http://127.0.0.1:8001')


# session 获取
@study_app.route(rule='/session_get')
def get_session():
    data = session.get('K')
    return data


# 异常处理 --> abort
@study_app.route(rule='/abort')
def error_msg():
    # abort 本质上类似于 raise 语句, 只能抛出符合http协议的异常状态码
    static_code = abort(404)
    return static_code


# 捕捉异常状态码, 返回新页面
@study_app.errorhandler(404)
def error_page(error):
    print(f'捕捉异常: {error}')
    return render_template('404.html')


@study_app.errorhandler(500)
def redirect_page(error):
    print(f'捕捉异常: {error}')
    return redirect(location='https://baidu.com')


# 请求钩子
# 请求前执行
@study_app.before_first_request
def first_request():
    pass
    # return 'Before First Request Run!'


@study_app.before_request
def before_request():
    pass
    # print('Before Request Run')


# 请求后执行
@study_app.after_request
def after_request(response):
    return response


@study_app.teardown_request
def teardown_request(error):
    return f'请求后异常信息: {error}'


# g 对象
def db_query():
    user_id = g.user_id
    user_name = g.user_name
    return user_id, user_name


@study_app.route(rule='/g')
def g_object():
    # g 对象来临时存储
    g.user_id = 1
    g.user_name  = 'Alice'
    db_query()
    return f'{g.user_id}, {g.user_name}'


# 程序入口
# 当文件独立运行时, 表达式成立
# 当文件被导入到其他文件中调用, 该表达式不成立, __name__ == app  # app: 文件名
# run方法:
# debug=True, 开启debug模式可以自动跟踪代码的变化, 定位错误信息
# host/post host可以指定主机地址, post可以指定服务端口, 
if __name__ == '__main__':
    # print(study_app.url_map)
    study_app.run(debug=True, host='0.0.0.0', port=8001)
