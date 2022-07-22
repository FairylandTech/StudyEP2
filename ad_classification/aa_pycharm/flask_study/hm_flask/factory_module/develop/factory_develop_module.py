from flask import Flask


class FactoryModules:

    def __init__(self):
        pass

    @staticmethod
    def create_app_develop(config_name):
        app_develop = Flask(import_name=__name__)
        app_develop.config.from_object(config_name)
        return app_develop
