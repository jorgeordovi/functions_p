def obtener_entero(texto):
    try:
        entero = int(texto)
    except ValueError:
        print("No se puede mapear a enero eun texto")
        entero = None
    return entero

print(obtener_entero("123"))
print(obtener_entero("abc"))