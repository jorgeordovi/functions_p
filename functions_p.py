def saludar():
    print("Hola Bebe")

saludar()

def nombres(nombre, apellido):
    print("Holas", nombre, apellido)

print("Jorge", "Codes")

def lista_d(*items, tareas):
    if len(items) > 1:
        print("Hoy haces", items[0], tareas[0])
    else:
        print("nada", items[0], tareas[1])

lista_d("trabajar", "ir al dentista") 