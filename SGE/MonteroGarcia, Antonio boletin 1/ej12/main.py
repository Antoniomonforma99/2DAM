#Escribe un programa que genere un número aleatorio entre 0 y 10 y nos pida adivinarlo Tenemos 3 intentos.

import random
intentos = 3
aleatorio = (random.randrange(10))
num = 14

print("El número generado es: ",aleatorio)

while aleatorio != int(num) and intentos > 0:
    print("Intenta averiguarlo")
    num = input()

    if aleatorio == int(num):
        print("Acertaste")

    intentos -= 1

