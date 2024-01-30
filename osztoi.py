import math


def osztok(szam):
    lista = []
    oszto = 2
    while (oszto <= math.sqrt(szam)):
        if szam % oszto == 0:
            lista.append(oszto)
        oszto += 1
    return lista

