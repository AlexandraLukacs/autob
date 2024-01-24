from Auto import Auto

def fajlbeolv():
    kocsi = []
    fajl=open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    fajl_lista=fajl.readlines()
    fajl.close()

    for i in range(0, len(fajl_lista), 1):
        aktsor=fajl_lista[i].strip().split("$")
        auto=Auto(aktsor[0], int(aktsor[1]))
        print(auto.nev, auto.gyart_datum)
        kocsi.append(auto)
    return kocsi

def tabla(lista, i):
    print(f"\t{lista[i].nev}: {len(lista[i].nev)} hosszú.")

def kiir(lista, i):
    f=open("kiir.txt", "w", encoding="utf-8")
    f.write(f"\t{lista[i].nev}: {len(lista[i].nev)} hosszú.")
    f.close()

def flotta(lista):
    print(f"\tAutók száma: {len(lista)}.")

def ertekes(lista):
    max:int = 0
    for i in range(0, len(lista), 1):
        if lista[i].gyart_datum > lista[max].gyart_datum:
            max = i
    return max