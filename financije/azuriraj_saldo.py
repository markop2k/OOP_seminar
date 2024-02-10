def update_saldo(cursor, trenutni_korisnik, saldo):
    query = """
            UPDATE korisnik
            SET saldo = ?
            WHERE korisnicko_ime = ?
            """
    cursor.execute(query, (saldo, trenutni_korisnik))
