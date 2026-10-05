"""Pelin data: asemat, vihjeet, tapahtumat ja tekstit.

Tässä tiedostossa ei ole logiikkaa, vain tietoa, jota muut tiedostot käyttävät.
Näin pelin sisältöä (esim. vihjeitä) on helppo muuttaa koskematta koodiin.
"""

# M1-linja idästä länteen. Indeksi 0 = Vuosaari, viimeinen = Kivenlahti.
ASEMAT = [
    "Vuosaari", "Rastila", "Puotila", "Itäkeskus", "Siilitie",
    "Herttoniemi", "Kulosaari", "Kalasatama", "Sörnäinen", "Hakaniemi",
    "Helsingin yliopisto", "Rautatientori", "Kamppi", "Ruoholahti",
    "Lauttasaari", "Koivusaari", "Keilaniemi", "Aalto-yliopisto",
    "Tapiola", "Urheilupuisto", "Niittykumpu", "Matinkylä",
    "Finnoo", "Kaitaa", "Soukka", "Espoonlahti", "Kivenlahti",
]
VIIMEINEN = len(ASEMAT) - 1  # viimeisen aseman indeksi (päätepysäkki)

# ---------- Pelin asetukset ----------
ALOITUSVUOROT = 24            # vuoroja tavalliselle pelaajalle
ALOITUSVUOROT_LAPSI = 30      # alle 13-vuotiaalle hieman enemmän
TAPAHTUMAN_TODENNAKOISYYS = 0.2   # satunnaisen tapahtuman todennäköisyys matkalla
TIEDON_TODENNAKOISYYS = 0.3       # "Tiesitkö?"-tiedon todennäköisyys matkalla
KAHVIN_VUOROT = 3             # kahvi antaa näin monta vuoroa (maksaa itse 1)
PUHELUT = 2                   # puhelimen akku riittää näin moneen puheluun

# Asemat, joilla on kahvila / järjestyksenvalvoja (pelin keksittyä sisältöä)
KAHVILA_ASEMAT = {"Itäkeskus", "Kamppi", "Tapiola", "Espoonlahti"}
VARTIJA_ASEMAT = {"Itäkeskus", "Rautatientori", "Tapiola", "Matinkylä"}

# ---------- Vihjeet etäisyyden mukaan ----------
VIHJEET = {
    "kuuma": [
        "KUUMA! Kuulet kuorsausta aivan läheltä!",
        "KUUMA! Penkillä on tuttu reppu ja avoin oppikirja!",
    ],
    "haalea": [
        "HAALEA. Joku haukotteli täällä äsken.",
        "HAALEA. Lattialla on yksi sukka... onko se tutorin?",
    ],
    "kylmä": [
        "KYLMÄ. Täällä on vain pirteitä matkustajia.",
        "KYLMÄ. Ei kuorsausta, ei tutoria.",
    ],
}

# ---------- Satunnaiset tapahtumat: (teksti, vuorojen muutos) ----------
TAPAHTUMAT = [
    ("Juna jäi hetkeksi jumiin tunneliin! (-1 vuoro)", -1),
    ("Löysit matkalipun lattialta! (+1 vuoro)", 1),
    ("Hissi on rikki, joudut ottamaan portaat. (-1 vuoro)", -1),
    ("Kuulutus: 'Hyvää iltaa kaikille!' Ei mitään erikoista.", 0),
]

# ---------- Kestävän kehityksen tiedot ----------
TIEDOT = [
    "Tiesitkö? Metro kulkee sähköllä, eikä se tuota pakokaasuja kaupungin kaduilla.",
    "Tiesitkö? Yksi metrojuna voi kuljettaa satoja ihmisiä kerralla.",
    "Tiesitkö? Joukkoliikenne tuottaa matkustajaa kohden yleensä vähemmän päästöjä kuin yksityisauto.",
    "Tiesitkö? Kestävän kehityksen tavoite 11 tarkoittaa kestäviä kaupunkeja ja yhteisöjä.",
    "Tiesitkö? Kävely ja pyöräily ovat päästöttömiä tapoja liikkua lyhyitä matkoja.",
    "Tiesitkö? Tyhjät pullot ja tölkit kuuluvat pantti- ja kierrätysjärjestelmään.",
]

# ---------- Reitit ja loppuratkaisut ----------
REITTINIMET = {
    "yksin": "Yksin tutkijana",
    "vartija": "Vartijan avulla",
    "puhelin": "Puhelun avulla",
    "tiimi": "Tiimityö (vartija + puhelin)",
}

# Pisteet-bonus reitin mukaan (yksin on vaikein, joten suurin bonus)
REITTIBONUS = {"yksin": 50, "vartija": 20, "puhelin": 20, "tiimi": 30}

LOPPUTEKSTIT = {
    "yksin": (
        "Löysit tutorin ihan omin avuin, {nimi}! Hän nukkuu penkillä reppu sylissä. "
        "Herätät hänet hellästi ja nousette yhdessä metroon kotiin. "
        "Joukkoliikenne vei teidät turvallisesti perille."
    ),
    "vartija": (
        "Järjestyksenvalvojan vinkki vei sinut perille, {nimi}! "
        "Tutori kuorsasi penkillä. Herätitte hänet yhdessä ja saatoitte hänet metroon kotiin."
    ),
    "puhelin": (
        "Puhelun soittoääni paljasti tutorin piilopaikan, {nimi}! "
        "Hän heräsi puhelimen ääneen ja hämmästyi: 'Onko metro jo menossa?' "
        "Nousitte yhdessä seuraavaan junaan."
    ),
    "tiimi": (
        "Vartija, puhelin ja oma älysi, {nimi}! Löysit tutorin upeaa tiimityötä käyttäen. "
        "Tutori kiittää ja lupaa nukkua jatkossa kotona omassa sängyssään."
    ),
}

HAVIOTEKSTI = (
    "Metro sulkeutui. Liian myöhäistä.\n"
    "Tutori oli asemalla {asema}. Onneksi aamulla järjestyksenvalvoja "
    "herätti hänet ja hän pääsi kotiin. Yritä uudelleen!"
)