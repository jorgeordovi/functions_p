## FUNCIONES DE ORDEN SUPERIOR

#MAP

from functools import reduce


def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12]

cuadrados = list(map(cuadrado, numeros))

#print(cuadrados)

def es_par(x):
    return x % 2 == 0

pares = list(filter(es_par, numeros))

print(pares)

## REDUCE: BINARY ARGUMENTS AND AN ITERABLE. APPLIES THE FUNCTITON ITERALY
# FROM LEFT TO RIGTH

def suma(x, y):
    return x + y 

sumatoria = reduce(suma, numeros)
print("sumatotria resul:", sumatoria)
    