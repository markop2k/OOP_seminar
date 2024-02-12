from .transakcija import Transakcija
def ispis_transakcija(cursor, trenutni_korisnik):
    # odabri

    query = """
            SELECT ime_kategorije, datum, dobitak, tip FROM dobitak WHERE korisnicko_ime = ?
            UNION ALL
            SELECT ime_kategorije, datum, trosak, tip FROM trosak WHERE korisnicko_ime = ?
            """
    cursor.execute(query, (trenutni_korisnik, trenutni_korisnik))
    transakcije = cursor.fetchall()

    print("Popis svih transakcija:")
    for transakcija in transakcije:
        ime_kategorije, datum, cijena, tip = transakcija[0], transakcija[1], transakcija[2], transakcija[3]
        data = Transakcija(ime_kategorije, datum, cijena, tip)
        data.ispis()

