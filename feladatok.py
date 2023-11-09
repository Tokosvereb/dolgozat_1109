def elsofeladat():
    print("***ELSŐ FELADAT***")
    print("Kérj be 1 páros számot a felhasználótól!")
    print("Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!")

    szam = int(input("Kérlek, adj meg egy páros számot: "))
    
    i = 0

    while i < 1:
        if  szam % 2 == 0:
            print("A bekért szám:", szam)
        else:
            print("A bekért szám nem osztható kettővel, kérlek adj meg egy másik számot!")
            
        i += 1

def masodikfeladat():
    print("***MÁSODIK FELADAT***")
    print("Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. ")
    print("Hány 3-mal osztható van közöttük? A kiírás formátuma:A számok között X db 3-mal osztható van!")
    import random
    import math

    i = 0
    harmasok = 0
    while i < 13:
        szam = math.floor(random.random( ) *149 + 10)
        print(f"Szám: {szam}")

        if szam == 3:
            harmasok += 3

        i+= 1
    print(f"Az hárommal oszthatók száma: {harmasok}")
    

def harmadikfeladat(szoveg, szam):
    print("***HARMADIK FELADAT***")
    print("Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot")
    print("Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”")

    szoveg = str(input("Adj meg egy nevet:"))
    szam = int(input("Adj meg egy számot:"))

    

            