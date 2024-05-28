import pymysql

def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        port=3306,
        db='sistema'
        )
    print("BD conectado exitosamente")
    return conn