import random

def random_lista():
    szamok = []
    print("\t", end="")
    for i in range(0, 50, 1):
        szam:int = int(random.randint(1, 100))
        szamok.append(szam)
        if i < 49:
            print(szam, end=", ")
        else:
            print(szam, end=" \n")
    return szamok

def ottel_oszthato(lista):
    db:int = 0
    for i in range(0, len(lista), 1):
        if lista[i] % 5 == 0:
            db += 1
    return db