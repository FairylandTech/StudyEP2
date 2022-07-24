import pymysql

class ConnectionMySQL:
    
    def __init__(self):
        pass
    
    @staticmethod
    def connect_mysql(host: str):
        
        connection_my_sql = pymysql.connect(
            host=host,
            user='root',
            password='root',
            port=13306,
            database='learn_db',
            charset='utf8',
        )
        
        
        return connection_my_sql


if __name__ == '__main__':
    pass
