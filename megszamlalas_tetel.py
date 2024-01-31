def megszamlalas():
    db = 0
    for i in range(10, 99, 2):
        if i % 2 == 0:
            db += 1
    return f"{db} db 2 jegyű páros szám van."

def min_kivalasztas():
    VEGE = 0
    db = 0
    min = 231233213
    while((szam := int(input("Szám: "))) != VEGE):
        if szam < min:
            min = szam
        db += 1
        print(f"{db} számból a legnagyobb: {min}")

