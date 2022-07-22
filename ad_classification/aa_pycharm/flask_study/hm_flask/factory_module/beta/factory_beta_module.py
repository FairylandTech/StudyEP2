from flask import Flask


class FactoryModules:

    def __init__(self):
        pass

    @staticmethod
    def create_app_beta(config_name):
        app_beta = Flask(import_name=__name__)
        app_beta.config.from_object(config_name)
        return app_beta
