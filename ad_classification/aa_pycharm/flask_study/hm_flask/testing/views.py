import testing
# 转换器
from werkzeug.routing import BaseConverter
# 自定义转换器
from config.testing.converter import TelConverter
from run_release_version_1_0_0 import study_app


study_app.url_map.converters['tel'] = TelConverter


@testing.test_api.route(rule='/root')
def test_root():
    return '测试主页'


@testing.test_api.route(rule='/testing/<string:user>/<int:number>/<tel:phone>')
def test_testing(user: str, number: int, phone: int):
    """
    testing
    :param user: 用户名 
    :param number: 页码
    :return: 
    """
    try:
        print(user, number, phone)
        print(type(user), type(number), type(phone))
        data = rf'Hello {user}, 当前在第{number}页, 手机号是{phone}'
        return data
    except Exception as e:
        print(e)
    


