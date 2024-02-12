from datetime import date
def unos_datuma():
    while True:
            try:
                dan = int(input(f'Unesite dan transakcije: '))
                mjesec = int(input(f'Unesite mjesec transakcije: '))
                godina = int(input(f'Unesite godinu transakcije: '))
                datum = date(godina, mjesec, dan).strftime("%Y.%m.%d.")

            except ValueError as e:
                print(e)
            else:
                return datum

def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj < min or broj > max:
                raise Exception(f"Morate upisati broj u intervalu {min}-{max}!")

        except ValueError:
            print('Unijeli ste znak, a ne cijeli broj!')

        except Exception as e:
            print(e)

        else:
            return broj

def unos_teksta(poruka):
    while True:
        try:
            tekst = input(poruka)

            if not tekst.isalpha():
                raise Exception("Morate unijeti samo slova!")

        except Exception as e:
            print(e)

        else:
            return tekst

def unos_znakova(poruka):
    while True:
        try:
            tekst = input(poruka)

            if len(tekst) == 0:
                raise Exception("Morate unijeti vise zankova!")

        except Exception as e:
            print(e)

        else:
            return tekst

def unos_realnog_pozitivnog_broja(poruka):
    while True:
        try:
            broj = float(input(poruka))

            if broj < 0:
                raise Exception('Morate upisati realni broj!')

        except ValueError:
            print('Unesli ste znak a ne realni broj.')
        except Exception as e:
            print(e)
        else:
            return broj
