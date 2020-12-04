class Ordenador(object):

    def __init__(self, memoria = 512, memoriaRAM = 8, procesador = "Intel i3 3300", precio = 499):
        self.memoria = memoria
        self.memoriaRAM = memoriaRAM
        self.procesador = procesador
        self.precio = precio

    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self, memoria):
        self._memoria = memoria

    @property
    def memoriaRAM(self):
        return self._memoriaRAM

    @memoriaRAM.setter
    def memoriaRAM(self, memoriaRAM):
        self._memoriaRAM = memoriaRAM

    @property
    def procesador(self):
        return self._procesador

    @procesador.setter
    def procesador(self, procesador):
        self._procesador = procesador

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def calcularPrecioVenta(self):
        return self.precio


class OrdenadorPortatil(Ordenador):

    def __init__(self, memoria = 512, memoriaRAM = 8, procesador = "Intel i3 3300", precio = 499, tamañoPantalla = 15.6):
        super().__init__(memoria, memoriaRAM, procesador, precio)
        self.tamañoPantalla = tamañoPantalla

    @property
    def tamañoPantalla(self):
        return self._tamañoPantalla

    @tamañoPantalla.setter
    def tamañoPantalla(self, tamañoPantalla):
        self._tamañoPantalla = tamañoPantalla

    def calcularPrecioVenta(self, porcentajeDescuento):
        return self.precio - (self.precio*(porcentajeDescuento/100))

class Tablet (Ordenador):
    def __init__(self, memoria = 128, memoriaRAM = 4, procesador = "AMD Quadcore", precio = 299, tamañoPantalla = 10, con_teclado = True):
        super().__init__(memoria, memoriaRAM, procesador, precio)
        self.tamañoPantalla = tamañoPantalla
        self.con_teclado = con_teclado

    @property
    def tamañoPantalla(self):
        return self._tamañoPantalla

    @tamañoPantalla.setter
    def tamañoPantalla(self, tamañoPantalla):
        self._tamañoPantalla = tamañoPantalla

    @property
    def con_teclado(self):
        return self._con_teclado

    @con_teclado.setter
    def con_teclado(self, con_teclado):
        self._con_teclado = con_teclado

    def calcularPrecioVenta(self, precioSeguro):
        return self.precio+precioSeguro
if __name__ == '__main__':

    ordenador = Ordenador()

    portatil = OrdenadorPortatil()

    tablet = Tablet()


    print(str(ordenador.calcularPrecioVenta()) +' euros')
    print(str(portatil.calcularPrecioVenta(10)) +' euros')
    print(str(tablet.calcularPrecioVenta(55)) +' euros')

