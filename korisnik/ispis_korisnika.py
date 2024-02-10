def ispis_korisnika(cursor, trenutni_korisnik):
    query = "SELECT korisnicko_ime, ime, prezime, saldo FROM korisnik WHERE korisnicko_ime = ?"
    cursor.execute(query, (trenutni_korisnik,))
    korisnici = cursor.fetchall()

    print(f"Informacije o korisniku:")
    for korisnik in korisnici:
        print(f"Korisničko ime: {korisnik[0]}  "
              f"\nIme i prezime: {korisnik[1]} {korisnik[2]}  "
              f"\nSaldo: {korisnik[3]}")

