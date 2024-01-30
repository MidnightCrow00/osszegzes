def kereses():
    also = 42
    felso = 67
    i = also
    while i <= felso and (i % 10 != 0):
        i += 1
    van = i <= felso
    if (van):
        print(f"van 0-ra végződő szám: {i}")
    else:
        print(f"nincs 0-ra végződő")