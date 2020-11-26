#Crea una función en python, triangulo, que reciba un número entero, e imprima un patrón como este por pantalla.
print("Introduzca el número para realizar la piramide")
num = int(input())

for i in range(num+1):
    print(i*"*")
for i in reversed(range(num+1)):
    print(i*"*")

