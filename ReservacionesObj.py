class ReservacionesObj:
    def _init_(
        self,
        id,
        nombre_evento,
        tipo_evento,
        fecha_inicio,
        fecha_final,
        hora_inicio,
        hora_final,
        fecha_reservacion,
        nombre_empresa,
        nombre_encargado,
    ):
        self.id = id
        self.nombreevento = nombre_evento
        self.tipoevento = tipo_evento
        self.fechainicio = fecha_inicio
        self.fechafinal = fecha_final
        self.horainicio = hora_inicio
        self.horafinal = hora_final
        self.fechareservacion = fecha_reservacion
        self.nombreempresa = nombre_empresa
        self.nombreencargado = nombre_encargado

    def idreservaciones(self):
        reservaciones = self.idreservaciones
        return reservaciones

