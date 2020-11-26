#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de
#una lista.

def suma (a):
    total = 0
    for i in (a):
        total += i
    return total

def multiplicacion (a):
    total = 1
    for i in (a):
        total *= i
    return total

print("Vamos a sumar y multiplicar una lista de 4 números")
print("Introduzca el primer numero")
num1 = int(input())
print("Introduzca el segundo numero")
num2 = int(input())
print("Introduzca el tercer numero")
num3= int(input())
print("Introduzca el cuarto numero")
num4 = int(input())


lista = [num1, num2, num3, num4]

print("La suma total es: ",suma(lista))
print("La multiplicación total es: ",multiplicacion(lista))
