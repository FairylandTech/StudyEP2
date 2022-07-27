from flask import Flask


# factory modules 
class FactoryModules:

    def __init__(self):
        pass

    @staticmethod
    def create_app_release(config_name):
        app_release = Flask(__name__)
        app_release.config.from_object(config_name)
        return app_release
