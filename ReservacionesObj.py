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
        self.nombreEvento = nombre_evento
        self.tipoEvento = tipo_evento
        self.fechaInicio = fecha_inicio
        self.fechaFinal = fecha_final
        self.horaInicio = hora_inicio
        self.horaFinal = hora_final
        self.fechaReservacion = fecha_reservacion
        self.nombreEmpresa = nombre_empresa
        self.nombreEncargado = nombre_encargado

    def getidReservaciones(self):
        idReservaciones = self.id
        return idReservaciones
