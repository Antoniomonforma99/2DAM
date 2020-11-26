#Definir una función inversa() que calcule la inversión de una cadena.

def inversa(cadena):
    cadena_inversa = cadena[::-1]
    return cadena_inversa

print("Ingrese una cadena de caractres")
cadena = input()

print(inversa(cadena))

