from Logic import Logic
from ReservacionesObj import ReservacionesObj


class ReservacionesLogic(Logic):
    def _init_(self):
        super()._init_()
        self.keys = [
            "id",
            "nombre_evento",
            "tipo_evento",
            "fecha_inicio",
            "fecha_final",
            "hora_inicio",
            "hora_final",
            "fecha_reservacion",
            "nombre_empresa",
            "nombre_encargado",
        ]


    def insertReservaciones(self, id, nombre_evento, tipo_evento, fecha_inicio, fecha_final, hora_inicio, hora_final, fecha_reservacion, nombre_empresa, nombre_encargado):
        database = self.get_databaseXObj()
        sql = (
            "INSERT INTO reservas_evento.registro_eventos (id, nombre_evento, tipo_evento, fecha_inicio_evento, fecha_final_evento, hora_inicio_evento, hora_final_evento, fecha_registro, encargado_empresa, nombre_empresa) "
            + f"VALUES (0, {nombre_evento}, {tipo_evento}, {fecha_inicio}, {fecha_final}, {hora_inicio}, {hora_final}, {fecha_reservacion}, {nombre_encargado}, {nombre_empresa});"
        )
        answer = database.executeNonQueryBool(sql)
        return answer



