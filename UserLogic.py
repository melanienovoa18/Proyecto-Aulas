from Logic import Logic
from UserObj import UserObj

class UserLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "iduser",
            "username",
            "password",
            "email",
        ]
    def getUserData(self, user):
        database = self.get_databaseXObj()
        sql = f"select * from reservas_eventos.usuario where username='{user}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            userObj = UserObj(
                data_dic["iduser"],
                data_dic["username"],
                data_dic["password"],
                data_dic["email"],
            )
            return userObj
        else:
            return None

    def getUserDataByID(self, id):
        database = self.get_databaseXObj()
        sql = f"select * from reservas_eventos.user where iduser='{id}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            userObj = UserObj(
                data_dic["iduser"],
                data_dic["username"],
                data_dic["password"],
                data_dic["email"],
            )
            return userObj
        else:
            return None

    def insertUser(
        self, usuario, password, email
    ):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO reservas_eventos.user (iduser, username, password, email) "
            + f"VALUES ('0', '{usuario}', '{password}', '{email}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer

    def updateUser(self, id, password, email):
        database = self.get_databaseXObj()
        sql = (
            "UPDATE reservas_eventos.user SET "
            + f"password = '{password}', "
            + f"email = '{email}' WHERE (iduser = '{id}');"
        )
        answer = database.executeNonQueryBool(sql)
        return answer
