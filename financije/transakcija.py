class Transakcija():
    def __init__(self, ime_kategorije, datum, cijena, tip):
        self.__ime_kategorije = ime_kategorije
        self.__datum = datum
        self.__cijena = cijena
        self.__tip = tip

    @property
    def ime_kategorije(self):
        return self.__ime_kategorije

    @ime_kategorije.setter
    def ime_kategorije(self, ime_kategorije):
        self.__ime_kategorije = ime_kategorije

    @property
    def datum(self):
        return self.__datum

    @datum.setter
    def datum(self, datum):
        self.__datum = datum

    @property
    def cijena(self):
        return self.__cijena

    @cijena.setter
    def cijena(self, cijena):
        self.__cijena = cijena

    @property
    def tip(self):
        return self.__tip

    @tip.setter
    def tip(self, tip):
        self.__tip = tip

    def ispis(self):
        print(f"\nIme kategorije: {self.ime_kategorije}")
        print(f"Datum: {self.datum}")
        print(f"Iznos: {self.cijena}")
        print(f"Tip: {self.tip}")
