#Pelaaja-luokka: pitää kirjaa pelaajan tilasta pelin aikana

from asemat import VIIMEINEN, PUHELUT


class Pelaaja:
    #Yksi pelaaja ja kaikki, mikä muuttuu pelin aikana

    def __init__(self, nimi, ika, paikka, vuorot):
        self.nimi = nimi
        self.ika = ika
        self.paikka = paikka      # aseman indeksi listassa ASEMAT
        self.vuorot = vuorot      # vuoroja jäljellä
        self.etsityt = set()      # asemat, joilta on jo etsitty
        self.vartijat = set()     # asemat, joilla vartijalta on jo kysytty
        self.kahvilat = set()     # asemat, joilla kahvi on jo juotu
        self.keinot = set()       # käytetyt apukeinot: "vartija", "puhelin"
        self.puheluja_jaljella = PUHELUT

    def liiku(self, suunta):

        #Siirtää pelaajaa (+1 eteenpäin, -1 taaksepäin).

        #Palauttaa True, jos siirto onnistui, ja False, jos ollaan päätepysäkillä.

        uusi_paikka = self.paikka + suunta
        if uusi_paikka < 0 or uusi_paikka > VIIMEINEN:
            return False
        self.paikka = uusi_paikka
        self.kayta_vuoro()
        return True

    def kayta_vuoro(self, maara=1):

        #Kuluttaa vuoroja (oletuksena yhden)
        self.vuorot -= maara

    def muuta_vuoroja(self, muutos):
        
        #Lisää tai vähentää vuoroja (tapahtumat, kahvi). Ei mene alle nollan
        self.vuorot = max(0, self.vuorot + muutos)

    def __str__(self):
        return f"{self.nimi} ({self.ika} v), vuoroja jäljellä: {self.vuorot}"