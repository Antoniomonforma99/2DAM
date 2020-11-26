#Escribe un programa en python que, dada una lista (y haciendo uso de la función type) imprima cada elemento de la
# lista, indicando su tipo.Por ejemplo, la lista podría ser la siguiente:
[1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

lista = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]


for i in (lista):
    print(type(i))
