def contador(n):
    print(n) #prints 1
    n += 1
    if n < 10:
        contador(n)

contador(1)