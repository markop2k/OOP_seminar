import sqlite3

from financije import unos_transakcije, ispis_transakcija, ispis_trosak
from korisnik import prijava, unos_registracije, provjeri_prijavu, odjava, ispis_korisnika
from utilities import unos_intervala

# Povezivanje s bazom podataka
conn = sqlite3.connect('faks.db')
cursor = conn.cursor()

running = True
trenutni_korisnik = None
while running:
    print('-' * 20)
    print('1. Prijava')
    print('2. Registracija')
    print('3. Informacije o korisniku')
    print('4. Unos dobitka')
    print('5. Unos troška')
    print('6. Ispis troškova')
    print('7. Ispis transakcija')
    print('8. Odjava')
    print('9. Kraj programa')
    print('-' * 20)
    print(trenutni_korisnik)
    akcija = unos_intervala(1, 9)

    if akcija == 1:
        if not provjeri_prijavu(trenutni_korisnik):
            trenutni_korisnik = prijava(cursor)
        else:
            print("Već ste prijavljeni.")

    elif akcija == 2:
        if not provjeri_prijavu(trenutni_korisnik):
            trenutni_korisnik = unos_registracije(cursor)
        else:
            print("Već ste prijavljeni.")

    elif akcija == 3:
        if provjeri_prijavu(trenutni_korisnik):
            ispis_korisnika(cursor, trenutni_korisnik)
        else:
            print("Niste prijavljeni")

    elif akcija == 4:
        if provjeri_prijavu(trenutni_korisnik):
            unos_transakcije(cursor, trenutni_korisnik, "dobitak")
        else:
            print("Niste prijavljeni")

    elif akcija == 5:
        if provjeri_prijavu(trenutni_korisnik):
            unos_transakcije(cursor, trenutni_korisnik, "trosak")
        else:
            print("Niste prijavljeni")

    elif akcija == 6:
        if provjeri_prijavu(trenutni_korisnik):
            ispis_trosak(cursor, trenutni_korisnik)
        else:
            print("Niste prijavljeni")

    elif akcija == 7:
        if provjeri_prijavu(trenutni_korisnik):
            ispis_transakcija(cursor, trenutni_korisnik)
        else:
            print("Niste prijavljeni")

    elif akcija == 8:
        if provjeri_prijavu(trenutni_korisnik):
            trenutni_korisnik = odjava()
        else:
            print("Niste prijavljeni")

    elif akcija == 9:
        running = False

# Zatvaranje veze s bazom podataka
conn.close()
