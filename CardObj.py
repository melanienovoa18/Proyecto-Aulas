class CardObj:
    def _init_(
        self,
        ID_tarjeta,
        numero_tarjeta,
        mes_vencimiento,
        annos_vencimiento,
        CCV,
    ):
        self.ID_tarjeta = ID_tarjeta
        self.numero_tarjeta = numero_tarjeta
        self.mes_vencimiento = mes_vencimiento
        self.annos_vencimiento = annos_vencimiento
        self.CCV = CCV

    def getNumeroTarjeta(self):
        numero_tarjeta = self.numero_tarjeta
        return numero_tarjeta

    def getCodigoSeguridad(self):
        CCV = self.CCV
        return CCV
    

