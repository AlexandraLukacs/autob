def elso_feladat():
    nev: str= str(input("\tAdja meg a felhasználónevét! "))
    jelszo: str= str(input("\tAdja meg a jelszavát! "))
    while not(nev == "bori99" and jelszo == "Szivecske<3"):
        print("\tBelépés megtagadva.")
        nev: str= str(input("\tAdja meg a felhasználónevét! "))
        jelszo: str= str(input("\tAdja meg a jelszavát! "))
    print("\tBelépés engedélyezve.")

        