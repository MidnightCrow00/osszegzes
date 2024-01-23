from Szamitogep import Szamitogep

peldany_1 = Szamitogep("win", 32)
peldany_2 = Szamitogep("mac", 16)
peldany_3 = Szamitogep("win", 16)
szamitogepek = []
szamitogepek.append(peldany_1)
szamitogepek.append(peldany_2)
szamitogepek.append(peldany_3)
for i in range(len(szamitogepek)):
    oprsz = szamitogepek[i].oprsz
    ram = szamitogepek[i].ram
    print(f"{oprsz} ({ram})")

# összegzés tétel
print("Átlag: ", end="")
gyujto = 0
for i in range(len(szamitogepek)):
    gyujto += szamitogepek[i].ram
print(f"{round(gyujto/len(szamitogepek),3)}")

# maximum kiválasztás tétel
print("Legtöbb ramot tartalmazó oprendszer: ", end="")
index = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > szamitogepek[index].ram:
        index = i
oprsz = szamitogepek[index].oprsz
print(f"{oprsz}")

# megszámlálás tétel
print(f"Hány Windows-os gépünk van?", end="")
windows = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].oprsz == "win":
        windows += 1
print(f"\t {windows} db ilyen gépünk van!")


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


