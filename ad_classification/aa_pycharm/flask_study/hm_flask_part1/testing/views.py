import testing
# 转换器
from werkzeug.routing import BaseConverter


@testing.test_api.route(rule='/root')
def test_root():
    return '测试主页'
    


