class RegistroObj:
    def __init__(
        self, id, nombre_empresa, giro, nit, num_registro, email, nombre_encargado,
    ):
        self.id = id
        self.nombreempresa = nombre_empresa
        self.giro = giro
        self.nit = nit
        self.numregistro = num_registro
        self.email = email
        self.nombreencargado = nombre_encargado

    def getnameempresa(self):
        name = self.nombreempresa
        return name
