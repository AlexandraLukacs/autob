import jelszo
import oszthato
import autom


print("ELső feladat:")
jelszo.elso_feladat()
print("")

print("Második feladat:")
lista=oszthato.random_lista()
db=oszthato.ottel_oszthato(lista)
print(f"A listában {db} darab öttel osztható szám van.")
print("")

print("Harmadik feladat:")
lista=autom.fajlbeolv()
print("III/Tabla:")
autom.tabla(lista, 4)
autom.kiir(lista, 4)
print("III/Flotta:")
autom.flotta(lista)
print("III/Értékes")
max=autom.ertekes(lista)
print(f"A legfiatalabb autó: {lista[max].nev}({lista[max].gyart_datum})")