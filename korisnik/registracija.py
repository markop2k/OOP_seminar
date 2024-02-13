from utilities import unos_teksta, unos_realnog_pozitivnog_broja, unos_znakova


def unos_registracije(cursor):
        korisnicko_ime = unos_znakova("Unesite novo korisničko ime: ")
        # Provjera postojanja korisničkog imena u bazi podataka
        query = "SELECT korisnicko_ime FROM korisnik WHERE korisnicko_ime = ?"
        cursor.execute(query, (korisnicko_ime,))
        korisnici = cursor.fetchall()

        if not korisnici:
                lozinka = unos_znakova("Unesite lozinku: ")
                ime = unos_teksta(f'Unesite ime korisnika: ').capitalize()
                prezime = unos_teksta(f'Unesite prezime korisnika: ').capitalize()
                saldo = unos_realnog_pozitivnog_broja(f'Unesite saldo: ')

                query = f'''
                        INSERT INTO korisnik (korisnicko_ime, lozinka, ime, prezime, saldo)
                        VALUES ('{korisnicko_ime}', '{lozinka}', '{ime}', '{prezime}','{saldo}')
                        '''
                cursor.execute(query)
                print("Registracija uspješna.")
                return korisnicko_ime

        else:
                print("Korisničko ime već postoji. Molimo odaberite drugo.")
                return
