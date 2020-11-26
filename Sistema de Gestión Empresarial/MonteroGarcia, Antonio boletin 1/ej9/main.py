#Implementar un programa en Python que pida un número indeterminado de cadenas de caracteres por el teclado, y cuando se
#finalice dicha introducción, muestre el listado de palabras.

print ("Introduzca una frase para a continuación mostrarla dividida en palabras")
frase = input()

fraseTroceada = frase.split()

print(fraseTroceada)
