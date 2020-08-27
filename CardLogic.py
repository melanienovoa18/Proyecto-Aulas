from Logic import Logic
from CardObj import CardObj

class CardLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "ID_pagos",
            "numero_tarjeta",
            "mes_vencimiento",
            "anos_vencimiento",
            "CCV",
        ]
    
    def insertCard(
        self, ID_pagos, numero_tarjeta, mes_vencimiento, anos_vencimiento, CCV
    ):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO reservas_evento.información_tarjeta (ID_pagos, numero_tarjeta, mes_vencimiento, años_vencimiento, CCV) "
            + f"VALUES ('0', {numero_tarjeta}, {mes_vencimiento}, {anos_vencimiento}, {CCV});"
        )
        answer = database.executeNonQueryBool(sql)
        return answer