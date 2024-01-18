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

print("Átlag: ", end="")
gyujto = 0
for i in range(len(szamitogepek)):
    gyujto += szamitogepek[i].ram
print(f"{round(gyujto/len(szamitogepek),3)}")

print("Legtöbb ramot tartalmazó oprendszer: ", end="")
index = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > szamitogepek[index].ram:
        index = i
oprsz = szamitogepek[index].oprsz
print(f"{oprsz}")