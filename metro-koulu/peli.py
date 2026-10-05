"""Peli-luokka: pelin pääsilmukka ja kaikki pelin toiminnot."""

import random

from .asemat import (
    ASEMAT, KAHVILA_ASEMAT, VARTIJA_ASEMAT, TAPAHTUMAT, TIEDOT,
    TAPAHTUMAN_TODENNAKOISYYS, TIEDON_TODENNAKOISYYS, KAHVIN_VUOROT,
    REITTINIMET, HAVIOTEKSTI, VIIMEINEN,
)
from .pelaaja import Pelaaja
from .apufunktiot import (
    laske_etaisyys, hae_vihje, arvo_tutorin_paikka, laske_aloitusvuorot,
    suunta_tekstiksi, maarita_reitti, laske_pisteet, hae_lopputeksti,
    kysy_valinta,
)
from .tiedostot import lue_teksti, tallenna_tulos


class Peli:
    """Yksi pelikerta. Luodaan uusi Peli-olio jokaiselle pelille."""

    def __init__(self, nimi, ika):
        self.aloitusvuorot = laske_aloitusvuorot(ika)
        aloituspaikka = random.randint(0, VIIMEINEN)
        self.pelaaja = Pelaaja(nimi, ika, aloituspaikka, self.aloitusvuorot)
        self.tutori = arvo_tutorin_paikka(aloituspaikka)  # tutorin aseman indeksi
        self.loydetty = False
        self.lopetettu = False

    # ---------- Näyttö ----------
    def nayta_tilanne(self):
        """Tulostaa nykyisen aseman ja vuorot."""
        p = self.pelaaja
        asema = ASEMAT[p.paikka]
        print("\n" + "-" * 40)
        print(f"Asema: {asema}")
        print(f"Vuoroja jäljellä: {p.vuorot}")
        if asema in VARTIJA_ASEMAT:
            print("Täällä on järjestyksenvalvoja.")
        if asema in KAHVILA_ASEMAT:
            print("Täällä on kahvila.")

    def nayta_valikko(self):
        """Tulostaa pelin valikon."""
        print("1) Eteenpäin (kohti Kivenlahtea)")
        print("2) Taaksepäin (kohti Vuosaarta)")
        print("3) Etsi tältä asemalta")
        print("4) Kysy järjestyksenvalvojalta")
        print("5) Soita tutorille")
        print("6) Osta kahvi")
        print("7) Ohjeet")
        print("0) Lopeta peli")

    # ---------- Pääsilmukka ----------
    def aja(self):
        """Pelin pääsilmukka. Jatkuu, kunnes tutori löytyy tai vuorot loppuvat."""
        while self.pelaaja.vuorot > 0 and not self.loydetty and not self.lopetettu:
            self.nayta_tilanne()
            self.nayta_valikko()
            valinta = kysy_valinta("> ", {"0", "1", "2", "3", "4", "5", "6", "7"})

            if valinta == "1":
                self._liiku(1)
            elif valinta == "2":
                self._liiku(-1)
            elif valinta == "3":
                self._etsi()
            elif valinta == "4":
                self._kysy_vartijalta()
            elif valinta == "5":
                self._soita()
            elif valinta == "6":
                self._osta_kahvi()
            elif valinta == "7":
                print(lue_teksti("ohjeet.txt"))
            elif valinta == "0":
                self.lopetettu = True
                print("Peli päättyi.")

        # Silmukan jälkeen selvitetään, miten peli päättyi
        if self.loydetty:
            self._voitto()
        elif not self.lopetettu:
            self._havio()

    # ---------- Toiminnot ----------
    def _liiku(self, suunta):
        """Liikkuu asemalta toiselle. Matkalla voi sattua jotain."""
        p = self.pelaaja
        if not p.liiku(suunta):
            print("Tämä on päätepysäkki! Siitä ei pääse enempää tähän suuntaan.")
            return
        print(f"Ajat asemalle {ASEMAT[p.paikka]}...")
        if random.random() < TAPAHTUMAN_TODENNAKOISYYS:
            teksti, muutos = random.choice(TAPAHTUMAT)
            print(teksti)
            p.muuta_vuoroja(muutos)
        if random.random() < TIEDON_TODENNAKOISYYS:
            print(random.choice(TIEDOT))

    def _etsi(self):
        """Etsii tutoria nykyiseltä asemalta (maksaa 1 vuoron)."""
        p = self.pelaaja
        if p.paikka in p.etsityt:
            print("Olet jo etsinyt täältä!")
            return
        p.etsityt.add(p.paikka)
        p.kayta_vuoro()
        etaisyys = laske_etaisyys(p.paikka, self.tutori)
        if etaisyys == 0:
            self.loydetty = True
        else:
            print(hae_vihje(etaisyys))

    def _kysy_vartijalta(self):
        """Reitti 2: järjestyksenvalvoja kertoo suunnan ja arvion etäisyydestä."""
        p = self.pelaaja
        if ASEMAT[p.paikka] not in VARTIJA_ASEMAT:
            print("Täällä ei ole järjestyksenvalvojaa.")
            return
        if p.paikka in p.vartijat:
            print("Vartija: 'Olen jo kertonut kaiken, mitä tiedän.'")
            return
        p.vartijat.add(p.paikka)
        p.kayta_vuoro()
        p.keinot.add("vartija")
        etaisyys = laske_etaisyys(p.paikka, self.tutori)
        if etaisyys == 0:
            print("Vartija: 'Täällä! Tällä asemalla nukkuu joku penkillä. Etsi tarkemmin!'")
        else:
            suunta = suunta_tekstiksi(p.paikka, self.tutori)
            # Vartijan arvio ei ole aivan tarkka (+/- 1 asema)
            arvio = max(1, etaisyys + random.choice([-1, 0, 1]))
            print(f"Vartija: 'Näin nuoren ihmisen nukahtavan junaan. "
                  f"Hän on {suunta}, noin {arvio} asemaa täältä.'")

    def _soita(self):
        """Reitti 3: tutorin puhelimen soittoääni paljastaa, onko hän lähellä."""
        p = self.pelaaja
        if p.puheluja_jaljella <= 0:
            print("Puhelimesi akku on lopussa!")
            return
        p.puheluja_jaljella -= 1
        p.kayta_vuoro()
        p.keinot.add("puhelin")
        etaisyys = laske_etaisyys(p.paikka, self.tutori)
        if etaisyys == 0:
            print("Soittoääni kuuluu aivan vierestä! Tutori on tällä asemalla!")
        elif etaisyys <= 2:
            print("Kuulet vaimean soittoäänen jostain lähistöltä...")
        else:
            print("Ei vastausta. Puhelin on varmaan äänettömällä.")
        print(f"(Puheluja jäljellä: {p.puheluja_jaljella})")

    def _osta_kahvi(self):
        """Kahvi antaa lisää vuoroja (maksaa 1, antaa KAHVIN_VUOROT)."""
        p = self.pelaaja
        if ASEMAT[p.paikka] not in KAHVILA_ASEMAT:
            print("Täällä ei ole kahvilaa.")
            return
        if p.paikka in p.kahvilat:
            print("Olet jo juonut kahvin täällä. Liikaa kahvia ei tee hyvää!")
            return
        p.kahvilat.add(p.paikka)
        p.kayta_vuoro()
        p.muuta_vuoroja(KAHVIN_VUOROT)
        print(f"Otat kahvin omaan termosmukiisi, joten kertakäyttökuppia ei tarvita. "
              f"(+{KAHVIN_VUOROT - 1} vuoroa nettona)")

    # ---------- Loppu ----------
    def _voitto(self):
        """Tulostaa voittoteksti, laskee pisteet ja tallentaa tuloksen."""
        p = self.pelaaja
        reitti = maarita_reitti(p.keinot)
        pisteet = laske_pisteet(p.vuorot, reitti)
        print("\n*** LÖYSIT HÄNET! ***")
        print(hae_lopputeksti(reitti, p.nimi))
        if p.vuorot == 0:
            print("Se oli viime hetkellä!")
        print(f"\nReitti: {REITTINIMET[reitti]}")
        print(f"Pisteet: {pisteet}")
        tallenna_tulos(p.nimi, p.ika, reitti, pisteet, p.vuorot)
        print("Tulos tallennettu tiedostoon tulokset.txt.")

    def _havio(self):
        """Tulostaa häviöteksti."""
        print("\n" + HAVIOTEKSTI.format(asema=ASEMAT[self.tutori]))