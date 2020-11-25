class Empleado(object):
    def __init__(self, nombre = "Antonio montero", sueldo_base = 1250, num_empleado = 25):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
        self.num_empleado = num_empleado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def sueldo_base(self):
        return self._sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo_base):
        self._sueldo_base = sueldo_base

    @property
    def num_empleado(self):
        return self._num_empleado

    @num_empleado.setter
    def num_empleado(self, num_empleado):
        self._num_empleado = num_empleado
    


    def calcular_sueldo(self):
        return self.sueldo_base


class Empleado_a_comision(Empleado):

     def __init__(self, nombre = "Fernando Fernández", sueldo_base = 1500, num_empleado = 39, incentivo = 10):
         super().__init__(nombre, sueldo_base, num_empleado)
         self.incentivo = incentivo

     @property
     def incentivo(self):
         return self._incentivo

     @incentivo.setter
     def incentivo(self, incentivo):
         self._incentivo = incentivo

     def calcular_sueldo(self):
        return self.sueldo_base + self.incentivo


class Empledo_fijo(Empleado):

    def __init__(self, nombre = "Mario Magdaleno", sueldo_base = 900, num_empleado = 45, impuestos = 21):
        super().__init__(nombre, sueldo_base, num_empleado)
        self.impuestos = impuestos

    @property
    def impuestos(self):
        return self._impuestos

    @impuestos.setter
    def impuestos(self, impuestos):
        self._impuestos = impuestos

    def calcular_sueldo(self):
        return self.sueldo_base - (self.sueldo_base * (self.impuestos/100))



if __name__ == '__main__':

    empleado = Empleado()
    a_comision = Empleado_a_comision()
    fijo = Empledo_fijo()

    empleados = [empleado, a_comision, fijo]

    print("Su sueldo de empleado es : "+str(empleado.calcular_sueldo()))
    print("Su sueldo de empleado a comision es : "+str(a_comision.calcular_sueldo()))
    print("Su sueldo de empleado fijo es : "+str(fijo.calcular_sueldo()))

    for i in empleados:
        if isinstance(i, Empleado_a_comision):
            print("El empleado "+i.nombre +" recibe un bono de 500 euros por ser de tipo a comisión")
