# encoding: utf-8
from flask import Flask
# step: 1 导入flask-restful
from flask_restful import Api, Resource

app = Flask(import_name=__name__)
# step: 2 实例化API 对象
api = Api(app)


# step: 3 定义视图类, 必须继承自Resource
class HomeIndexPage(Resource):
    # 定义 method 方法
    def get(self):
        # 返回响应字符串, 默认转为json
        # return 'Hello World'
        return {'hello': 'world'}
    
# step: 4 添加路由
api.add_resource(HomeIndexPage, '/home')


# main
if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, host='0.0.0.0', port=8001)