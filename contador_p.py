def contador(n):
    print(n)
    n += 1
    if n < 10:
        contador(n)

contador(1)