class Julkaisu():
    def __init__(self, nimi):
        self.nimi = nimi 

    def tulosta_tiedot(self):
        print(f"Julkaisu nimi on {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
    
    def tulosta_tiedot(self):
        print(f"Nimi on {self.nimi}, Kirjoittaja on {self.kirjoittaja}, ja Sivumäärä on {self.sivumaara}")
    
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi on {self.nimi}, Päätoimittaja on {self.paatoimittaja}")

lehti1 = Lehti("aku ankka", "aki hyyppä")
kirja1 = Kirja("hyyti on 6", "Roosa", 200)

lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()