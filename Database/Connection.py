import pymysql

def connection():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        port = 3306,
        db = "sistema_administrativo"
    )
    print("DB connectec")
    return conn