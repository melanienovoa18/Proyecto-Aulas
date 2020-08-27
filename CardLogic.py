from Logic import Logic
from CardObj import CardObj


class CardLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "numero_tarjeta",
            "mes_vencimiento",
            "annos_vencimiento",
            "CCV",
        ]
    
    def insertCard(
        self, numero_tarjeta, mes_vencimiento, annos_vencimiento, CCV
    ):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO reservas_evento.informacion_tarjeta (ID_tarjeta, numero_tarjeta, mes_vencimiento, annos_vencimiento, CCV) "
            + f"VALUES (0, {numero_tarjeta}, {mes_vencimiento}, {annos_vencimiento}, {CCV});"
        )
        answer = database.executeNonQueryBool(sql)
        return answer 
