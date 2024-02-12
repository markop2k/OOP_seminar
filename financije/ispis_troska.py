from .transakcija import Transakcija
from utilities import unos_datuma

def ispis_trosak(cursor, trenutni_korisnik):
    #print("Unesi datum od kada želite ispis troška")
    #period_krece = unos_datuma()
    #print("Unesi datum do kada želite ispis troška")
    #period_zavrsava = unos_datuma()
    
    query = """
            SELECT ime_kategorije, datum, trosak, tip FROM trosak 
            INNER JOIN korisnik ON trosak.korisnicko_ime = korisnik.korisnicko_ime
            WHERE korisnik.korisnicko_ime = ?
            """
    cursor.execute(query, (trenutni_korisnik,))
    troskovi = cursor.fetchall()
    ukupni_trosak = 0
    print("Popis svih transakcija:")
    for trosak in troskovi:
        ime_kategorije, datum, cijena, tip = trosak
        data = Transakcija(ime_kategorije, datum, cijena, tip)
        data.ispis()
        ukupni_trosak += cijena

    print(f"Ukupni trosak od"
            f"Iznos:{ukupni_trosak}")

