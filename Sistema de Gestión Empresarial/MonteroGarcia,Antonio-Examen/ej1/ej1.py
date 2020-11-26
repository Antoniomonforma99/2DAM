
num = int(input("Introduzca un número de 4 cifras"))

listaAux = []

def grande(num):
    resul=0
    listaAux.clear()
    for cifra in range(1,5):
        listaAux.append(cifra)
    listaAux.sort(reverse = True)
    return listaAux

def pequenya (num):
    listaAux.clear()
    for cifra in range(1,5):
        listaAux.append(cifra)
    listaAux.sort()
    return listaAux

def diferencia(num):
    listaAux.clear()
    mayor = grande(num)
    menor = pequenya(num)

    for i in range(1,5):
        listaAux[i] = mayor[i] - menor[i]

    return listaAux

def mediano(num):
    return (grande(num)+pequenya(num)/2)





print("El valor más grande que se puede formas es: ", int(grande(num)))
print("El valor más pequeño que se puede formas es: ",pequenya(num))
print("El número mediano es: ",mediano(num))
print("La diferencia entre el mayor y el menor es: ",diferencia(num))

