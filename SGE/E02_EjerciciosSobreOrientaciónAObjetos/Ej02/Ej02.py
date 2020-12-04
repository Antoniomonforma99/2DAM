class Documento (object):

    def __init__(self, nombre_empresa = "BioDAM", direccion = "C/ Condes de Bustillo 13", num_tlf = 954345465):
        self.nombre_empresa = nombre_empresa
        self.direccion = direccion
        self.num_tlf = num_tlf
    @property
    def nombre_empresa(self):
        return self._nombre_empresa

    @nombre_empresa.setter
    def nombre_empresa(self, nombre_empresa):
        self._nombre_empresa = nombre_empresa

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion (self, direccion):
        self._direccion = direccion

    @property
    def num_tlf(self):
        return self._num_tlf

    @num_tlf.setter
    def num_tlf(self, num_tlf):
        self._num_tlf = num_tlf

    def __str__(self):
        mensaje = self.nombre_empresa + '\n' + self.direccion \
                  + '\n' + str(self.num_tlf)
        return mensaje


class TarjetaDeVisita(Documento):

    def __init__(self, nombre_empresa = "BioDAM", direccion = "C/ Condes de Bustillo 13", num_tlf = 954345465,
                 nombre = "Antonio Montero García"):
        super().__init__(nombre_empresa, direccion, num_tlf)
        self.nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

        def __str__(self):
            mensaje = self.nombre_empresa + '\n' + self.direccion + '\n' + str(self.num_tlf) + '\n' + self.nombre
            return mensaje

    def __str__(self):
        mensaje = self.nombre_empresa + '\n' + self.direccion + '\n' + str(self.num_tlf) + '\n' + self.nombre
        return mensaje

class Carta(Documento):

    def __init__(self, nombre_empresa = "BioDAM", direccion = "C/ Condes de Bustillo 13", num_tlf = 954345465,
                 nombre = "Antonio Montero García", fecha = "19/11/2020"):
        super().__init__(nombre_empresa, direccion, num_tlf)
        self.nombre = nombre
        self.fecha = fecha

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    def __str__(self):
        mensaje = self.nombre_empresa + '\n' + self.direccion + '\n' + str(self.num_tlf) + '\n' + self.nombre + '\n' + self.fecha
        return mensaje


if __name__ == '__main__':

    documento = Documento()
    tarjeta = TarjetaDeVisita()
    carta = Carta()

    print(documento)
    print()
    print(tarjeta)
    print()
    print(carta)
