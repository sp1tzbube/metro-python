import random

class Esine():
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino
    
    def __str__(self):
        return f"{self.nimi} ({self.paino}kg)"

class Huone():
    def __init__(self, nimi, esineet=None):
        self.nimi = nimi
        self.esineet = esineet if esineet else []

class Pelaaja():
    def __init__(self, nimi, age, sijainti ):
        self.nimi = nimi
        self.age = age
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self,huone):
        self.sijainti = huone 
        print(f"--> Siirryit paikkaan {huone.nimi}")
    
    def keraa_esine(self,esine):
        self.sijainti.esineet.remove(esine)
        self.esineet.append(esine)
        print(f"--> Keräsit esineen: {esine.nimi}")

def koe():
    print("--> Koe tulee ensi viikolla")

def tunti():
    print("--> Nyt on Python-tunti")

def ope():
    print("--> Sinun opesi ovat Haavisto Aino ja Heinonen Ava")

def koulu():
    print("--> Sinun koulu on Metropolia")

def pisteet():
    print(f"--> Sinun pisteesi: {random.randint(0, 100)}/100")

def arvonta():
    print(f"--> Onnenlukusi on: {random.randint(1, 5)}")


huoneet = [
    Huone("Rautatientori", [Esine("Matkakortti", 0.1), Esine("Kartta", 0.2)]),
    Huone("Kamppi", [Esine("Kahvikuppi", 0.4)]),
    Huone("Helsingin yliopisto", [Esine("Kirja", 1.5), Esine("Kello", 0.3)]),
]

nimi = input("Anna nimesi: ")
age = int(input("Anna ikäsi: "))

if age < 12:
    print("Olet alaikäinen, peli sulkeutuu.")
    exit()

pelaaja = Pelaaja(nimi, age, huoneet[0])
print(f"Tervetuloa, {pelaaja.nimi}!")




w = ""
while w != "lopeta":
    print("\n--------- Päävalikko ---------")
    print(f"Sijainti: {pelaaja.sijainti.nimi}")
    print("Komennot: koe, tunti, ope, koulu, pisteet, arvonta, liiku, kerää, lopeta")
    w = input("Anna komento: ")
    print("--------- ---------  ---------")

    if w == "koe":
        koe()

    elif w == "tunti":
        tunti()

    elif w == "ope":
        ope()

    elif w == "koulu":
        koulu()

    elif w == "pisteet":
        pisteet()

    elif w == "arvonta":
        arvonta()

    elif w == "liiku":
        print("Minne haluat mennä?")
        for i, huone in enumerate(huoneet):
            print(f"  {i}. {huone.nimi}")
        try:
            numero = int(input("Anna numero: "))
            pelaaja.liiku(huoneet[numero])
        except (ValueError, IndexError):
            print("--> Virheellinen valinta!")

    elif w == "kerää":
        esineet = pelaaja.sijainti.esineet
        if not esineet:
            print("--> Täällä ei ole esineitä")
        else:
            print("Täällä on:")
            for i, esine in enumerate(esineet):
                print(f"  {i}. {esine}")
            try:
                numero = int(input("Minkä esineen keräät (numero): "))
                pelaaja.keraa_esine(esineet[numero])
            except (ValueError, IndexError):
                print("--> Virheellinen valinta!")

    elif w == "lopeta":
        print("--> Nähdään taas!")

    else:
        print("--> Virhe!")

print(f"Sun nimesi on {pelaaja.nimi}, ja ikäsi on {pelaaja.age}")