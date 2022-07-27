from flask import Flask
from config import app_config
from public.path_file.root_path import ROOT_PATH

# factory modules 
class FactoryModules:
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def create_study(config_name):
        study = Flask(__name__, template_folder=f'{ROOT_PATH}templates')
        study.config.from_object(config_name)
        return study
    
    