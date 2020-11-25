class Vehiculo (object):
    def __init__(self, precio = 35):
        self.precio = precio

    @property
    def precio (self):
        return self._precio

    @precio.setter
    def precio (self, precio):
        self._precio = precio

    def calcularImpuesto(self):
        return self.precio


class Motocicleta(Vehiculo):

    def __init__(self, precio = 35, potencia = 49):
        super().__init__(precio)
        self.potencia = potencia

    @property
    def potencia (self):
        return  self._potencia

    @potencia.setter
    def potencia (self, potencia):
        self._potencia = potencia

    def calcularImpuesto(self):
        return self.precio + (self.potencia * 0.6)


class Furgoneta (Vehiculo):

    def __init__(self, precio = 35, cantidadFija = 20):
        super().__init__(precio)
        self.cantidadFija = cantidadFija

    @property
    def cantidadFija (self):
        return self._cantidadFija

    @cantidadFija.setter
    def cantidadFija (self, cantidadFija):
        self._cantidadFija = cantidadFija

    def calcularImpuesto(self):
        return self.precio + self.cantidadFija


class Coche (Vehiculo):

    def __init__(self, precio = 35, cilindrada = 280):
        super().__init__(precio)
        self.cilindrada = cilindrada

    @property
    def cilindrada (self):
        return  self._cilindrada

    @cilindrada.setter
    def cilindrada (self, cilindrada):
        self._cilindrada = cilindrada

    def calcularImpuesto(self):
        return self.precio + (self.cilindrada * 0.25)


if __name__ == '__main__':

    vehiculo = Vehiculo()
    motocicleta = Motocicleta()
    furgoneta = Furgoneta()
    coche  = Coche()

    print("EL precio de la revisión del vehiculo es de: "+str(vehiculo.calcularImpuesto()))
    print("EL precio de la revisión de la motocicleta es de: "+str(motocicleta.calcularImpuesto()))
    print("EL precio de la revisión de la furgontea es de: "+str(furgoneta.calcularImpuesto()))
    print("EL precio de la revisión  del coche es de: "+str(coche.calcularImpuesto()))
