def division(dividiendo, divisor):
    try:
        resultado = dividiendo / divisor
    except ZeroDivisionError:
        print("Error: no se puede imprimir 0")
        resultado = None
    return resultado
    
print(division(5, 0))

print("Important message")