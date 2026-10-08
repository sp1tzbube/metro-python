#Etsi väsynyt tutori - pääohjelma ja päävalikko.

from peli import Peli
from apufunktiot import kysy_valinta, kysy_nimi, kysy_ika
from tiedostot import lue_teksti, lue_tulokset
from asemat import REITTINIMET


def nayta_tulokset():

    #Tulostaa viisi parasta tulosta tiedostosta tulokset.txt
    tulokset = lue_tulokset()

    if not tulokset:
        print("\n---> Ei vielä tuloksia. Pelaa ensin!")
        return
    
    # Järjestetään pisteiden mukaan suurimmasta pienimpään
    tulokset.sort(key=lambda t: t["pisteet"], reverse=True)
    print("\n============ ============ PARHAAT TULOKSET ============ ============")

    for numero, tulos in enumerate(tulokset[:5], start=1):
        reitti = REITTINIMET.get(tulos["reitti"], tulos["reitti"])
        print(f"{numero}. {tulos['nimi']} ({tulos['ika']} v) - "
              f"{tulos['pisteet']} p - {reitti}")


def paavalikko(nimi, ika):

    #Päävalikon silmukka. Palauttaa True, jos halutaan vaihtaa pelaajaa

    while True:
        print(f"\n============ ============ PÄÄVALIKKO ============ ============ (pelaaja: {nimi}, {ika} v)")
        print("1) Aloita peli")
        print("2) Ohjeet")
        print("3) Parhaat tulokset")
        print("4) Vaihda pelaajaa")
        print("0) Lopeta")
        valinta = kysy_valinta("> ", {"0", "1", "2", "3", "4"})

        if valinta == "1":
            peli = Peli(nimi, ika)
            peli.aja()

        elif valinta == "2":
            print(lue_teksti("ohjeet.txt"))

        elif valinta == "3":
            nayta_tulokset()

        elif valinta == "4":
            return True
        
        elif valinta == "0":
            return False


def main():

    #Ohjelman aloituspiste: esittely, nimi, ikä ja päävalikko
    print(lue_teksti("intro.txt"))
    jatka = True

    while jatka:
        nimi = kysy_nimi()
        ika = kysy_ika()
        print(f"\nHei {nimi}! Aloitetaan.")
        jatka = paavalikko(nimi, ika)
    print("---> Kiitos pelaamisesta! Näkemiin!")


if __name__ == "__main__":
    main()