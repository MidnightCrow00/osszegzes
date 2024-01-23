from Szamitogep import Szamitogep

def peldanyositas():
    peldany_1 = Szamitogep("win", 32)
    peldany_2 = Szamitogep("mac", 16)
    peldany_3 = Szamitogep("win", 16)

    szamitogepek = []
    szamitogepek.append(peldany_1)
    szamitogepek.append(peldany_2)
    szamitogepek.append(peldany_3)

    return szamitogepek

def lista_kiiras(szamitogepek):
    for i in range(len(szamitogepek)):
        oprsz = szamitogepek[i].oprsz
        ram = szamitogepek[i].ram
        print(f"{oprsz} ({ram})")

    gepek_listaja = peldanyositas()
    lista_kiiras(gepek_listaja)