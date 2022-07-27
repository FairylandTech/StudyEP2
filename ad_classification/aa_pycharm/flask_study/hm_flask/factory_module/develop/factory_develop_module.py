from flask import Flask
from public.path_file.root_path import ROOT_PATH


class FactoryModules:

    def __init__(self):
        pass

    @staticmethod
    def create_app_develop(config_name):
        app_develop = Flask(import_name=__name__, template_folder=f'{ROOT_PATH}/templates')
        app_develop.config.from_object(config_name)
        return app_develop
