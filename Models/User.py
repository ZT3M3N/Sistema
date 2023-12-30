class User():
    def __init__(self, conn):
        self.conn = conn
            
    def getUser(self,user,password):
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE user_name = %s AND password = %s"
            cursor.execute(sql,(user,password))
            result = cursor.fetchone()
            return result