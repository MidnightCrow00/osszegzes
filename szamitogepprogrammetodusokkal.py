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
def osszegze(szamitogepek):
    # összegzés tétel
    print("Átlag: ", end="")
    gyujto = 0
    for i in range(len(szamitogepek)):
        gyujto += szamitogepek[i].ram
    print(f"{round(gyujto / len(szamitogepek), 3)}")

def maximum_kivalasztas(szamitogepek):
    # maximum kiválasztás tétel
    print("Legtöbb ramot tartalmazó oprendszer: ", end="")
    index = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > szamitogepek[index].ram:
            index = i
    oprsz = szamitogepek[index].oprsz
    print(f"{oprsz}")

def megszamlalas(szamitogepek):
    # megszámlálás tétel
    print(f"Hány Windows-os gépünk van?", end="")
    windows = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].oprsz == "win":
            windows += 1
    print(f"\t {windows} db ilyen gépünk van!")

def eldontes(szamitogepek):
    # eldöntés tétel
    vizsgalt_ram = 16
    print(f"Van-e {vizsgalt_ram} GB-nál nagyobb windows?\t", end="")
    van = False
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > vizsgalt_ram and szamitogepek[i].oprsz == "win":
            van = True
    if van == True:
        print(f"Van ilyen gép!")
    else:
        print("Nincs ilyen gép!")