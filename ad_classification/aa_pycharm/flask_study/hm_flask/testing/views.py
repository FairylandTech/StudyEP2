import testing
# 转换器
from werkzeug.routing import BaseConverter


@testing.test_api.route(rule='/root')
def test_root():
    return '测试主页'


@testing.test_api.route(rule='/testing/<string:user>/<int:number>')
def test_testing(user: str, number: int):
    try:
        print(user, number)
        print(type(user), type(number))
        data = rf'Hello {user}, 当前在第{number}页'
        return data
    except Exception as e:
        print(e)
    


