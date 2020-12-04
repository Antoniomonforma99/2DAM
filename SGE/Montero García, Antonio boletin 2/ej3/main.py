#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocal_o_no(a):
    vocal = False

    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
        vocal = True
    return vocal

print("Introduce una letra")
letra = input()

if vocal_o_no(letra)==True:
    print("La letra: ",letra ," es una vocal")
else:
    print("La letra: ",letra ," no es una vocal")

