#Implementa una función que calcule el factorial de un número. Recuerda que el factorial de un número es el producto de
#todos los números desde ese número hasta 1. Por ejemplo, el factorial de 3, 3!, es 6

print("Introduzca un número para mostrar su factorial")
num = input()
factorial = 1
uno = 1
for i in range(1, int(num)+1):
    factorial = factorial*i

print("The factorial of",num,"is",factorial)
