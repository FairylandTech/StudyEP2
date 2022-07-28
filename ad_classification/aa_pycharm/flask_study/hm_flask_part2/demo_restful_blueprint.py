from flask import Flask, Blueprint
from flask_restful import Api, Resource

app = Flask(import_name=__name__)
index_bp = Blueprint(name='index_bp', import_name=__name__)

api = Api(index_bp)

class IndexResource(Resource):
    
    def get(self):
        return {'get': 'Hello World'}
    
    def post(self):
        return {'post': 'Hello World'}
    
    
api.add_resource(IndexResource, '/index')
app.register_blueprint(blueprint=index_bp)

# main
if __name__ == '__main__':
    print(app.url_map)
    app.run()