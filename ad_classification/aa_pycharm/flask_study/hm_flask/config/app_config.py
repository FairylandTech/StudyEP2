class DefaultConfig:
    
    def __init__(self):
        pass
    
    MYSQL_URL = 'mysql address'
    REDIS_URL = 'redis address'
    
    # Session 
    SECRET_KEY = 'secret key'
    

class ProductionConfig:
    
    def __init__(self):
        pass
    
    
    MYSQL_URL = 'produce mysql address'
    REDIS_URL = 'produce redis address'


