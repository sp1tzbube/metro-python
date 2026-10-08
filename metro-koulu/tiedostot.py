
#Tiedostojen lukeminen ja kirjoittaminen.
# - Tekstit (intro.txt, ohjeet.txt) luetaan kansiosta tekstit/
# - Tulokset kirjoitetaan tiedostoon tulokset.txt ja luetaan sieltä


from pathlib import Path

# Projektin juurikansio 
JUURI = Path(__file__).resolve().parent
TEKSTIKANSIO = JUURI / "tekstit"
TULOSTIEDOSTO = JUURI / "tulokset.txt"


def lue_teksti(tiedostonimi):
    #Lukee tekstitiedoston kansiosta tekstit/ ja palauttaa sen sisällön
    polku = TEKSTIKANSIO / tiedostonimi
    try:
        with open(polku, encoding="utf-8") as tiedosto:
            return tiedosto.read()
    except FileNotFoundError:
        return f"[Tiedostoa {tiedostonimi} ei löytynyt]"


def tallenna_tulos(nimi, ika, reitti, pisteet, vuoroja_jaljella):
    
    # -Lisää yhden tuloksen tulokset.txt-tiedoston loppuun.

    # -Rivin muoto: nimi;ika;reitti;pisteet;vuoroja_jäljellä

    rivi = f"{nimi};{ika};{reitti};{pisteet};{vuoroja_jaljella}\n"
    with open(TULOSTIEDOSTO, "a", encoding="utf-8") as tiedosto:
        tiedosto.write(rivi)


def lue_tulokset():
    
    # -Lukee kaikki tulokset ja palauttaa ne listana sanakirjoja.

    # -Virheelliset rivit ohitetaan. Jos tiedostoa ei ole, palautetaan tyhjä lista.

    tulokset = []
    try:
        with open(TULOSTIEDOSTO, encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                osat = rivi.strip().split(";")
                if len(osat) != 5:
                    continue
                try:
                    tulokset.append({
                        "nimi": osat[0],
                        "ika": int(osat[1]),
                        "reitti": osat[2],
                        "pisteet": int(osat[3]),
                        "vuorot": int(osat[4]),
                    })
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    return tulokset