"""Apufunktiot: pienet, erillisesti testattavat funktiot.

Funktiot saavat tietonsa parametreina ja palauttavat tuloksen return-lauseella.
"""

import random

from .asemat import (
    VIIMEINEN, VIHJEET, ALOITUSVUOROT, ALOITUSVUOROT_LAPSI,
    REITTIBONUS, LOPPUTEKSTIT,
)


def laske_etaisyys(paikka_a, paikka_b):
    """Palauttaa kahden aseman välisen etäisyyden asemina."""
    return abs(paikka_a - paikka_b)


def hae_vihje(etaisyys):
    """Palauttaa satunnaisen vihjeen etäisyyden mukaan (kuuma/haalea/kylmä)."""
    if etaisyys <= 2:
        taso = "kuuma"
    elif etaisyys <= 6:
        taso = "haalea"
    else:
        taso = "kylmä"
    return random.choice(VIHJEET[taso])


def arvo_tutorin_paikka(pelaajan_paikka):
    """Arpoo tutorin aseman. Se ei ole sama kuin pelaajan asema.

    Tutori on voinut nukahtaa ja ajaa päätepysäkille, joten sen
    todennäköisyys on suurempi (25 %).
    """
    if random.random() < 0.25 and pelaajan_paikka != VIIMEINEN:
        return VIIMEINEN
    while True:
        paikka = random.randint(0, VIIMEINEN)
        if paikka != pelaajan_paikka:
            return paikka


def laske_aloitusvuorot(ika):
    """Palauttaa aloitusvuorojen määrän iän mukaan."""
    if ika < 13:
        return ALOITUSVUOROT_LAPSI
    return ALOITUSVUOROT


def suunta_tekstiksi(pelaajan_paikka, tutorin_paikka):
    """Kertoo, missä suunnassa tutori on pelaajaan nähden."""
    if tutorin_paikka > pelaajan_paikka:
        return "kohti Kivenlahtea"
    return "kohti Vuosaarta"


def maarita_reitti(keinot):
    """Päättelee pelaajan reitin käytettyjen apukeinojen perusteella."""
    if "vartija" in keinot and "puhelin" in keinot:
        return "tiimi"
    if "vartija" in keinot:
        return "vartija"
    if "puhelin" in keinot:
        return "puhelin"
    return "yksin"


def laske_pisteet(vuoroja_jaljella, reitti):
    """Pisteet = 10 pistettä jokaisesta jäljellä olevasta vuorosta + reittibonus."""
    return vuoroja_jaljella * 10 + REITTIBONUS[reitti]


def hae_lopputeksti(reitti, nimi):
    """Palauttaa reitin loppuratkaisun tekstin pelaajan nimellä."""
    return LOPPUTEKSTIT[reitti].format(nimi=nimi)


def kysy_valinta(kehote, sallitut):
    """Kysyy valintaa, kunnes käyttäjä antaa sallitun arvon. Palauttaa valinnan."""
    while True:
        valinta = input(kehote).strip()
        if valinta in sallitut:
            return valinta
        print("En ymmärrä. Valitse listasta.")


def kysy_nimi():
    """Kysyy pelaajan nimen, kunnes se ei ole tyhjä. Palauttaa nimen."""
    while True:
        nimi = input("Nimesi: ").strip()
        if nimi:
            # Puolipiste varataan tulostiedoston erottimeksi
            return nimi.replace(";", ",")
        print("Nimi ei voi olla tyhjä.")


def kysy_ika():
    """Kysyy pelaajan iän numerona (5-120). Palauttaa iän kokonaislukuna."""
    while True:
        teksti = input("Ikäsi: ").strip()
        if teksti.isdigit() and 5 <= int(teksti) <= 120:
            return int(teksti)
        print("Anna ikä numerona (5-120).")