#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(a, b, c):
    mayor = 0
    if a>b and b>c:
        mayor = a
    elif b>c:
        mayor = b
    else:
        mayor = c

    return mayor

print("Indica el primer número")
a = int(input())

print("Indica el segundo número")
b = int(input())

print("Indica el tercer número")
c = int(input())

print("El valor mayor es: " ,max_de_tres(a, b, c))
