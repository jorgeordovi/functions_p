#DECORADOR 

def decorador(funcion):
    def envoltotio():
       print("This comes first an parameter")
       funcion()
       print("This comes after given  parameter")
    return envoltotio

def saludar():
    print("Hola, estoy saludando")

saludo_decorado = decorador(saludar)

saludo_decorado()
