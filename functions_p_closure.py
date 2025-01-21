#CLOSURE

def exterior(x):
    def interior(y):
        return x + y
    return interior

#CREAMOS CLAUSULA LLAMANDO A LA FUANCION EXERIOR
clausura = exterior(10)

#WHEN EW CALL THE CUNTION IT GONNA REMEMEBER THE GIVEN VALUE

resulado = clausura(5)

print(resulado)
