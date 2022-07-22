class DefaultConfig:

    def __init__(self):
        pass

    MYSQL_URL = 'mysql address'
    REDIS_URL = 'redis address'


class DevelopmentConfig:

    def __init__(self):
        pass

    MYSQL_URL = 'development mysql address'
    REDIS_URL = 'development redis address'
    
    
class ProductionConfig:

    def __init__(self):
        pass

    MYSQL_URL = 'produce mysql address'
    REDIS_URL = 'produce redis address'


