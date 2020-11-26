class Cuenta(object):
    def __init__(self, num_cuenta, titular, cantidad = 0):
        self._num_cuenta = num_cuenta
        self._titular = titular
        self._cantidad = cantidad

    @property
    def num_cuenta(self):
        return self._num_cuenta

    @num_cuenta.setter
    def num_cuenta(self, num_cuenta):
        self._num_cuenta = num_cuenta

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    def __str__(self):
        return "El titular " +self._titular +" con nº de cuenta " +self._num_cuenta +" tiene un saldo de " +self._cantidad + " euros"

    def comprobar_que_cuenta_es_mayor(self, c1, c2):
        if (c1.cantidad > c2.cantidad):
            mayor = c1
        else:
            mayor = c2
        return mayor


if __name__ == '__main__':
    cuenta1 = Cuenta("12345","Antonio Montero", "120")
    cuenta2 = Cuenta("98765","Manuel López" , "250")
    print(cuenta1.titular)
    print(cuenta2.titular)
    print(cuenta1)
    print(cuenta2)
    print("La cuenta con mayor cuenta es la de " +cuenta1.comprobar_que_cuenta_es_mayor(cuenta1,cuenta2).titular)
