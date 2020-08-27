from Logic import Logic
from RegistroObj import RegistroObj

class UserLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "nombre_empresa",
            "giro",
            "nit",
            "num_registro",
            "email",
            "nombre_encargado",
        ]

    def getRegistroData(self, nombre_empresa):
        database = self.get_databaseXObj()
        sql = f"select * from reservas_eventos.usuario where username='{usuario}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            registerObj = UserObj(
                data_dic["id"],
                data_dic["nombre_empresa"],
                data_dic["giro"],
                data_dic["num_registro"],
                data_dic["email"],
                data_dic["nombre_encargado"],
            )
            return registerObj
        else:
            return None

    def getRegistroDataByID(self, id):
        database = self.get_databaseXObj()
        sql = f"select * from reservas_eventos.user where iduser='{id}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            registroObj = UserObj(
                data_dic["id"],
                data_dic["nombre_empresa"],
                data_dic["giro"],
                data_dic["nit"],
                data_dic["num_registro"],
                data_dic["email"],
                data_dic["nombre_encargado"],
            )
            return registroObj
        else:
            return None

    def insertRegistro(
        self, nombre_empresa, giro, nit, num_registro, email, nombre_encargado
    ):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO reservas_eventos.user (id, nombre_empresa, giro, nit, num_registro, email, nombre_encargado) "
            + f"VALUES ('0', '{nombre_empresa}', '{giro}', '{nit}', '{num_registro}', '{email}', '{nombre_encargado}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def updateRegistro(self, id, nombre_empresa, giro, nit, num_registro, email, nombre_encargado):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE reservas_eventos.registro_eventos SET "
            + f"password = '{password}', "
            + f"email = '{email}' WHERE (iduser = '{id}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer
