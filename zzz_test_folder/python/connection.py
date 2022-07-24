import pymysql
from testing import ConnectionMySQL




if __name__ == '__main__':
    line = ConnectionMySQL.connect_mysql(host='10.31.101.2')
    cursor = line.cursor()
    sql_state = "show databases ;"
    cursor.execute(sql_state)
    result = cursor.fetchall()
    for i in result:
        i = i[0]
        print(i)
    cursor.close()
    line.close()
    