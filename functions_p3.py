from unittest import result


def ret_shop(shopping):
    for item in shopping:
        print(item)

lista_fruits = ["Manzana", "Pera", "Banana"]

ret_shop(lista_fruits)

def cuantos(a,b):
    resultado = a + b
    return resultado

resultado = cuantos(2,3)
print(resultado)

def calcular_resultado(a,b,/,*,c,d): # de la barra <-- solo pueden ser positional arguments, del * -> keyword #
    print(a + b + c + d)

calcular_resultado(1, 2, c = 3, d = 4)