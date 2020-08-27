import mysql.connector

class Database:
    def __createCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="reservas_evento"
)
        cursor = con.cursor()
        return con, cursor

    def registro_usuario():