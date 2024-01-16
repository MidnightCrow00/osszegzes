def osszegzo():
    i = 0
    n = 0
    ossz = 0
    n = int(input("N = "))
    while (n < 0):
        n = int(input("N = "))
    for i in range(0, n + 1):
        ossz += i
    return f"Az első {n} db ternészetes szám összege: {ossz}"

