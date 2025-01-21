# funcion es com o argumento


def do_function(func, valor):
    return func(valor)

def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

print(do_function(cuadrado, 3)) # salida 9
print(do_function(cubo, 3)) # salida 27
