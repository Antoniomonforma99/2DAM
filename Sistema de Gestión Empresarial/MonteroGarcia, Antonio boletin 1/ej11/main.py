#Escribe un programa que pida primero un número entero y después pida números enteros hasta que la suma de los números
#introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.

print("Introduzca un número entero")
num = input()
aux = 0

while num != aux:
    print("Introduzca un número")
    aux = input()
    aux+=aux
    print(aux)


