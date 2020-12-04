#Escribe un programa que sea capaz de escribir los N primeros números de la sucesión de fibonacci.

print("¿Cuántos valores de la serie quiere?")
num = int(input())

aux = 0
aux2 = 1

for i in range(num):
    print(aux)
    numAux= aux+aux2

    aux = aux2
    aux2 = numAux
