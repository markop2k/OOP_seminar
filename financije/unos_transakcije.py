from utilities import unos_datuma, unos_realnog_pozitivnog_broja, unos_znakova
from .azuriraj_saldo import update_saldo


def unos_transakcije(cursor, trenutni_korisnik, tip, dobitak=None, trosak=None):
    ime_kategorije = unos_znakova("Unesite ime kategorije: ").upper()
    datum = unos_datuma()

    # Trazi saldo iz database
    query = "SELECT saldo FROM korisnik WHERE korisnicko_ime = ?"
    cursor.execute(query, (trenutni_korisnik,))
    saldo_row = cursor.fetchone()

    if saldo_row: # Ako ima slado
        saldo = saldo_row[0]
        print(saldo)

    else: # Ako nema saldo
        saldo = 0  # Set a default value for saldo or handle it as appropriate
        print("No saldo found for the user")

    try:
        if tip == "dobitak": #Ako je odabran unos dobitka
            cijena = unos_realnog_pozitivnog_broja("Koliki je dobitak: ")
            saldo += float(cijena)
            #Upis u database
            query = "INSERT INTO dobitak (korisnicko_ime, ime_kategorije, datum, dobitak, tip) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (trenutni_korisnik, ime_kategorije, datum, cijena, tip))
            update_saldo(cursor, trenutni_korisnik, saldo)

        elif tip == "trosak": #Ako je odabran unos troska
            cijena = unos_realnog_pozitivnog_broja("Koliki je trosak: ")
            saldo -= float(cijena)
            # Upis u database
            query = "INSERT INTO trosak (korisnicko_ime, ime_kategorije, datum, trosak, tip) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (trenutni_korisnik, ime_kategorije, datum, cijena, tip))
            update_saldo(cursor, trenutni_korisnik, saldo)

    except Exception as e:
        # Handle any exceptions that might occur during database operations
        print("Pogreška kod unosa u bazu  podataka, ponovite", e)

