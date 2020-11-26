class Empleado (object):
    def __init__(self, nombre, apellidos, departamento, antiguedad, salario_base_anual = 10302.60):
        self._nombre = nombre
        self._apellidos = apellidos
        self._departamento = departamento
        self._antiguedad = antiguedad
        self._salario_base_anual = salario_base_anual

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos

    @nombre.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def departamento(self):
        return self._departamento

    @nombre.setter
    def departamento(self, departamento):
        self._departamento = departamento

    @property
    def antiguedad(self):
        return self._antiguedad

    @nombre.setter
    def antiguedad(self, antiguedad):
        self._antiguedad = antiguedad

    @property
    def salario_base_anual(self):
        return self._salario_base_anual

    @nombre.setter
    def salario_base_anual(self, salario_base_anual):
        self._salario_base_anual = salario_base_anual

    def salario_neto_mensual(self, empleado):
        sueldo = empleado.salario_base_anual / 14

        trienios = empleado.antiguedad//3
        sueldo = sueldo +(trienios * 35.14)

        if (sueldo < 12449.99):
            sueldo = sueldo - (sueldo * (19/100))
        elif (sueldo > 12449.99 and sueldo < 20199.99):
            sueldo = sueldo - (sueldo * (24/100))
        elif (sueldo > 20199.99 and sueldo < 35199.99):
            sueldo = sueldo - (sueldo * (30/100))
        elif (sueldo > 35199.99 and sueldo < 59999.99):
            sueldo = sueldo - (sueldo * (37/100))
        else:
            sueldo = sueldo - (sueldo * (45/100))

class Comercial (Empleado):
    def __init__(self, nombre, apellidos, departamento, antiguedad, salario_base_anual, porcentaje_sobre_ventas, objetivo_ventas):
        super(nombre, apellidos, departamento, antiguedad, salario_base_anual)
        self._porcentaje_sobre_ventas = porcentaje_sobre_ventas
        self._objetivo_ventas = objetivo_ventas
    @property
    def porcentaje_sobre_ventas(self):
        return self._porcentaje_sobre_ventas

    @porcentaje_sobre_ventas.setter
    def porcentaje_sobre_ventas(self, porcentaje_sobre_ventas):
        self._porcentaje_sobre_ventas = porcentaje_sobre_ventas

    @property
    def objetivo_ventas(self):
        return self._objetivo_ventas

    @objetivo_ventas.setter
    def objetivo_ventas(self, objetivo_ventas):
        self._objetivo_ventas = objetivo_ventas

    def salario_neto_mensual(self, empleado, total_vendido):
        sueldo = empleado.salario_base_anual / 14

        trienios = empleado.antiguedad//3
        sueldo = sueldo +(trienios * 35.14)

        if (sueldo < 12449.99):
            sueldo = sueldo - (sueldo * (19/100))
        elif (sueldo > 12449.99 and sueldo < 20199.99):
            sueldo = sueldo - (sueldo * (24/100))
        elif (sueldo > 20199.99 and sueldo < 35199.99):
            sueldo = sueldo - (sueldo * (30/100))
        elif (sueldo > 35199.99 and sueldo < 59999.99):
            sueldo = sueldo - (sueldo * (37/100))
        else:
            sueldo = sueldo - (sueldo * (45/100))

        if (total_vendido > empleado.objetivo_ventas):
            sueldo = sueldo + (empleado.porcentaje_sobre_ventas * (45/100))

class Directivo (Empleado):
    def __init__(self, nombre, apellidos, departamento, antiguedad, salario_base_anual, numero_empleado_a_cargo = 5):
        super(nombre, apellidos, departamento, antiguedad, salario_base_anual)
        self._numero_empelados_a_cargo = numero_empleado_a_cargo

    @property
    def numero_empleados_a_cargo(self):
        return self._numero_empelados_a_cargo

    @numero_empleados_a_cargo.setter
    def numero_empleados_a_cargo(self, numero_empleados_a_cargo):
        self._numero_empelados_a_cargo = numero_empleados_a_cargo


if __name__ == '__main__':

    empleado = Empleado("Antonio Montero", "logística", 10, 17999.55)
    comercial = Comercial("Manuel López", "i+d", 5, 10995, 15, 12)
    directivo = Directivo("Rafael Ramírez", "logística", 12, 34000, 7)
    print(str(empleado.salario_neto_mensual(empleado)))


