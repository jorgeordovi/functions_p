def suma_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n-1)

print(suma_naturales(5))
#bulcle de iteracion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))