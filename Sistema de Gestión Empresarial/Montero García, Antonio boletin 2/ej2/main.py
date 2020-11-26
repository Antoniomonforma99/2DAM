#Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función
# len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def longitud_cadena(a):
    cont = 0
    for i in a:
        cont+=1
    return cont

print("Introduzca una cadena de caracteres")
a = input()

print("La cadena: ",a ,", tiene: ",longitud_cadena(a) ," caracteres")
