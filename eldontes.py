import math


def szamitas():
    n = int(input("\n Szám: "))
    prim = True
    if n < 2:
        prim = False
    else:
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            i += 1
        prim = i > math.sqrt(n)
    if prim == True:
        print("Prím")
    else:
        print('Nem prím')