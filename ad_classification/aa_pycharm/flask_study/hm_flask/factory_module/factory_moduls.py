from flask import Flask
from config import app_config

# factory modules 
class FactoryModules:
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def create_study(config_name):
        study = Flask(__name__)
        study.config.from_object(config_name)
        return study
    
    