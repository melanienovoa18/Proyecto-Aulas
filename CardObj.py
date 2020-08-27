class CardObj:
    def _init_(
        self,
        ID_pagos,
        numero_tarjeta,
        mes_vencimiento,
        anos_vencimiento,
        CCV,
    ):
        self.ID_pagos = ID_pagos
        self.numero_tarjeta = numero_tarjeta
        self.mes_vencimiento = mes_vencimiento
        self.anos_vencimiento = anos_vencimiento
        self.CCV = CCV

    def getNumeroTarjeta(self):
        numero_tarjeta = self.numero_tarjeta
        return numero_tarjeta

    def getCodigoSeguridad(self):
        CCV = self.CCV
        return CCV
    

