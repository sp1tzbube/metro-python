import os
import random

# Tiedostot haetaan samasta kansiosta kuin tämä ohjelma
KANSIO = os.path.dirname(os.path.abspath(__file__))


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
    def __init__(self, nimi, age, sijainti):
        self.nimi = nimi
        self.age = age
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, huone):
        self.sijainti = huone
        print(f"--> Siirryit paikkaan {huone.nimi}")

    def keraa_esine(self, esine):
        self.sijainti.esineet.remove(esine)
        self.esineet.append(esine)
        print(f"--> Keräsit esineen: {esine.nimi}")


# ---------- Tekstitiedostojen luku ----------

def nayta_tiedosto(tiedostonimi):
    """Lukee tekstitiedoston ja tulostaa sen sisällön."""
    polku = os.path.join(KANSIO, tiedostonimi)
    try:
        with open(polku, "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())
    except FileNotFoundError:
        print(f"--> Tiedostoa {tiedostonimi} ei löytynyt")


# ---------- Tallennus ja lataus ----------

def tallennuspolku(nimi):
    """Tekee pelaajan nimestä turvallisen tiedostonimen."""
    puhdas = "".join(m for m in nimi.lower() if m.isalnum())
    return os.path.join(KANSIO, f"tallennus_{puhdas}.txt")


def esineet_tekstiksi(esineet):
    return ";".join(f"{e.nimi}:{e.paino}" for e in esineet)


def tekstista_esineet(teksti):
    esineet = []
    if teksti:
        for osa in teksti.split(";"):
            nimi, paino = osa.split(":")
            esineet.append(Esine(nimi, float(paino)))
    return esineet


def tallenna(pelaaja, huoneet):
    rivit = [
        f"nimi={pelaaja.nimi}",
        f"ika={pelaaja.age}",
        f"sijainti={pelaaja.sijainti.nimi}",
        f"reppu={esineet_tekstiksi(pelaaja.esineet)}",
    ]
    for huone in huoneet:
        rivit.append(f"huone={huone.nimi}|{esineet_tekstiksi(huone.esineet)}")

    with open(tallennuspolku(pelaaja.nimi), "w", encoding="utf-8") as tiedosto:
        tiedosto.write("\n".join(rivit) + "\n")
    print("--> Peli tallennettu")


def lataa(nimi, huoneet):
    """Lataa tallennuksen. Palauttaa Pelaaja-olion tai None, jos lataus ei onnistu."""
    try:
        with open(tallennuspolku(nimi), "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.read().splitlines()

        tiedot = {}
        for rivi in rivit:
            avain, arvo = rivi.split("=", 1)
            if avain == "huone":
                huoneen_nimi, esineteksti = arvo.split("|", 1)
                for huone in huoneet:
                    if huone.nimi == huoneen_nimi:
                        huone.esineet = tekstista_esineet(esineteksti)
            else:
                tiedot[avain] = arvo

        sijainti = next(h for h in huoneet if h.nimi == tiedot["sijainti"])
        pelaaja = Pelaaja(tiedot["nimi"], int(tiedot["ika"]), sijainti)
        pelaaja.esineet = tekstista_esineet(tiedot["reppu"])
        return pelaaja
    except FileNotFoundError:
        return None
    except (ValueError, KeyError, StopIteration):
        print("--> Tallennustiedosto on virheellinen")
        return None


# ---------- Komennot ----------

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


def nayta_reppu(pelaaja):
    if not pelaaja.esineet:
        print("--> Reppusi on tyhjä")
    else:
        print("Reppusi sisältö:")
        for esine in pelaaja.esineet:
            print(f"  - {esine}")


def luo_huoneet():
    return [
        Huone("Rautatientori", [Esine("Matkakortti", 0.1), Esine("Kartta", 0.2)]),
        Huone("Kamppi", [Esine("Kahvikuppi", 0.4)]),
        Huone("Helsingin yliopisto", [Esine("Kirja", 1.5), Esine("Kello", 0.3)]),
    ]


# ---------- Pelin aloitus ----------

huoneet = luo_huoneet()

nayta_tiedosto("intro.txt")
nayta_tiedosto("ohjeet.txt")

nimi = input("Anna nimesi: ")
pelaaja = None

if os.path.exists(tallennuspolku(nimi)):
    vastaus = input(f"Löytyi tallennettu peli pelaajalle {nimi}. Jatketaanko (k/e)? ")
    if vastaus.lower() == "k":
        pelaaja = lataa(nimi, huoneet)
        if pelaaja:
            print(f"Tervetuloa takaisin, {pelaaja.nimi}!")
        else:
            huoneet = luo_huoneet()  # lataus epäonnistui, aloitetaan alusta

if pelaaja is None:
    while True:
        try:
            age = int(input("Anna ikäsi: "))
            break
        except ValueError:
            print("--> Anna ikä numerona!")

    if age < 12:
        print("Olet alaikäinen, peli sulkeutuu.")
        exit()

    pelaaja = Pelaaja(nimi, age, huoneet[0])
    print(f"Tervetuloa, {pelaaja.nimi}!")


w = ""
while w != "lopeta":
    print("\n--------- Päävalikko ---------")
    print(f"Sijainti: {pelaaja.sijainti.nimi}")
    print("Komennot: koe, tunti, ope, koulu, pisteet, arvonta, reppu, liiku, kerää, ohjeet, tallenna, lopeta")
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

    elif w == "reppu":
        nayta_reppu(pelaaja)

    elif w == "ohjeet":
        nayta_tiedosto("ohjeet.txt")

    elif w == "tallenna":
        tallenna(pelaaja, huoneet)

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
        tallenna(pelaaja, huoneet)
        print("--> Nähdään taas!")

    else:
        print("--> Virhe!")

print(f"Sun nimesi on {pelaaja.nimi}, ja ikäsi on {pelaaja.age}")