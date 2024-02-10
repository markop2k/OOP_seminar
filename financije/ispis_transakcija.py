from utilities import unos_datuma
def ispis_transakcija(cursor, trenutni_korisnik):
    # Provjera postojanja korisničkog imena u bazi podataka
    query = """
            SELECT ime_kategorije, datum, dobitak, tip FROM dobitak WHERE korisnicko_ime = ?
            UNION ALL
            SELECT ime_kategorije, datum, trosak, tip FROM trosak WHERE korisnicko_ime = ?
            """
    cursor.execute(query, (trenutni_korisnik, trenutni_korisnik))
    transakcije = cursor.fetchall()


    print("Popis svih transakcija:")
    for transakcija in transakcije:
        print("Informacije o transakciji:")
        print(f"Ime kategorije: {transakcija[0]}")
        print(f"Datum: {transakcija[1]}")
        print(f"Iznos: {transakcija[2]}")
        print(f"Tip: {transakcija[3]}")
