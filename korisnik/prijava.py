from utilities import unos_znakova



def prijava(cursor):
    korisnicko_ime = unos_znakova(f'Unesite korisničko ime: ')
    lozinka = unos_znakova(f'Unesite lozinku: ')

    # Izvršavanje SQL upita za provjeru korisnika
    query = "SELECT korisnicko_ime FROM korisnik WHERE korisnicko_ime = ? AND lozinka = ?"
    cursor.execute(query, (korisnicko_ime, lozinka))
    korisnici = cursor.fetchall()
    if not korisnici:  # ako je ispravno korisničko ime
        print("Pogrešno korisničko ime ili lozinka")
        return None
    else:
        print(f"Prijavljeni ste kao {korisnicko_ime}")
        return korisnicko_ime


def odjava():
    trenutni_korisnik = None
    print("Odjavili ste se.")
    return trenutni_korisnik


def provjeri_prijavu(trenutni_korisnik):
    return trenutni_korisnik is not None