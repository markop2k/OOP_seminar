from utilities import unos_datuma, unos_realnog_pozitivnog_broja, unos_znakova
from .azuriraj_saldo import update_saldo
from .transakcija import Transakcija

def unos_transakcije(cursor, trenutni_korisnik, tip):
    ime_kategorije = unos_znakova("Unesite ime kategorije: ").upper()
    datum = unos_datuma()

    # Trazi saldo iz database
    query = "SELECT saldo FROM korisnik WHERE korisnicko_ime = ?"
    cursor.execute(query, (trenutni_korisnik,))
    provjera_slado = cursor.fetchone()

    if provjera_slado: # Ako ima slado
        saldo = provjera_slado[0]
        print(saldo)

    else: # Ako nema saldo
        saldo = 0
        print("Nije pronađeno saldo")

    if tip == "dobitak": #Ako je odabran unos dobitka
        cijena = unos_realnog_pozitivnog_broja("Koliki je dobitak: ")
        saldo += float(cijena)
            #Upis u database
        query = "INSERT INTO dobitak (korisnicko_ime, ime_kategorije, datum, dobitak, tip) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (trenutni_korisnik, ime_kategorije, datum, cijena, tip))
        update_saldo(cursor, trenutni_korisnik, saldo)
        return Transakcija(ime_kategorije, datum, cijena, tip)

    elif tip == "trosak": #Ako je odabran unos troska
        cijena = unos_realnog_pozitivnog_broja("Koliki je trosak: ")
        saldo -= float(cijena)
            # Upis u database
        query = "INSERT INTO trosak (korisnicko_ime, ime_kategorije, datum, trosak, tip) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (trenutni_korisnik, ime_kategorije, datum, cijena, tip))
        update_saldo(cursor, trenutni_korisnik, saldo)
        return Transakcija(ime_kategorije, datum, cijena, tip)

