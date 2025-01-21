def es_par(numeros):
    return numeros % 2 ==0

def es_primo(numeros):
    if numeros < 2:
        return False
    for i in range(1, int(numeros**0.5) + 1)
        if numeros % i == 0:
            return False
    return True
        