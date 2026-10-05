# Etsi väsynyt tutori

Komentorivillä pelattava seikkailupeli, joka sijoittuu Helsingin ja Espoon M1-metrolinjalle (Vuosaari - Kivenlahti, 27 asemaa).

## Pelin idea ja tarina

Perjantai-iltana tutorisi on opiskellut koko päivän ja on aivan uupunut. Hän nousi M1-metroon ja nukahti penkille. Nyt hän ei vastaa puhelimeen. Metro sulkeutuu keskiyöllä, ja silloin tutori jäisi asemalle yksin.

## Tavoite

Löydä tutori ennen kuin vuorot (aika) loppuvat. Vuorot kuvaavat aikaa keskiyöhön: jokainen siirtyminen asemalta toiselle, etsintä, kysyminen tai soittaminen kuluttaa yhden vuoron.

Peli sopii myös alaikäisille (K12): tarina on rauhallinen eikä sisällä väkivaltaa tai päihteitä.

## Käynnistys

Vaatimukset: Python 3.8 tai uudempi, ei ulkoisia kirjastoja.

```
python main.py
```

## Toiminnallisuudet

- Päävalikko: aloita peli, ohjeet, parhaat tulokset, vaihda pelaajaa, lopeta
- Pelaajan nimi ja ikä kysytään alussa. Alle 13-vuotias saa enemmän vuoroja (30 vs. 24).
- Tutorin sijainti arvotaan joka pelissä uudelleen. Pelaajan aloitusasema arvotaan myös.
- Tutori on voinut ajaa päätepysäkille, joten Kivenlahti on todennäköisempi paikka (25 %).
- Vihjeet kuuma / haalea / kylmä etäisyyden mukaan
- Satunnaiset tapahtumat matkalla (juna jumissa, löytynyt lippu jne.)
- Kahvi antaa lisää vuoroja kahvilaasemilla
- Tulokset tallennetaan tiedostoon `tulokset.txt`, ja päävalikosta näkee viisi parasta

### Kolme reittiä voittoon

| Reitti | Miten | Pisteet-bonus |
|---|---|---|
| Yksin tutkijana | Etsitään asemilta ja tulkitaan vihjeitä | +50 |
| Vartijan avulla | Kysytään järjestyksenvalvojalta suuntaa ja etäisyyttä | +20 |
| Puhelun avulla | Soitetaan tutorille ja kuunnellaan soittoääntä | +20 |
| Tiimityö | Käytetään sekä vartijaa että puhelinta | +30 |

Jokaisella reitillä on oma loppuratkaisun teksti. Lisäksi on häviöloppu, jos metro sulkeutuu ennen kuin tutori löytyy.

Pisteet = 10 pistettä jokaisesta jäljellä olevasta vuorosta + reittibonus.

## Kestävän kehityksen näkökulma

Peli liittyy YK:n kestävän kehityksen tavoitteeseen **11: kestävät kaupungit ja yhteisöt** sekä **13: ilmastotekoihin**:

- Koko peli tapahtuu joukkoliikenteessä (metro), joka kulkee sähköllä ja vähentää yksityisautoilun tarvetta.
- Loppuratkaisuissa tutori ja pelaaja matkustavat kotiin metrolla.
- Matkan varrella pelaaja näkee "Tiesitkö?"-tietoja joukkoliikenteestä, kävelystä ja kierrätyksestä.
- Kahvi juodaan omaan termosmukiin, jolloin kertakäyttökuppeja ei tarvita.

## Ohjelman rakenne

```
tutori_peli/
├── main.py              pääohjelma ja päävalikko
├── readme.md
├── tulokset.txt         luodaan automaattisesti, kun peli on voitettu
├── tekstit/
│   ├── Intro.txt        pelin esittely
│   └── ohjeet.txt       pelin ohjeet
└── peli/                paketti
    ├── __init__.py
    ├── asemat.py        data: asemat, vihjeet, tapahtumat, tekstit
    ├── pelaaja.py       luokka Pelaaja
    ├── peli.py          luokka Peli, pääsilmukka ja toiminnot
    ├── apufunktiot.py   apufunktiot (parametrit ja paluuarvot)
    └── tiedostot.py     tiedostojen luku ja kirjoitus
```

### Luokat

- **Pelaaja**: nimi, ikä, sijainti, vuorot, käytetyt apukeinot. Metodit: `liiku`, `kayta_vuoro`, `muuta_vuoroja`.
- **Peli**: yksi pelikerta. Sisältää pelaajan, tutorin sijainnin ja pääsilmukan `aja()`. Metodit toiminnoille: `_liiku`, `_etsi`, `_kysy_vartijalta`, `_soita`, `_osta_kahvi`.

### Funktiot

`laske_etaisyys`, `hae_vihje`, `arvo_tutorin_paikka`, `laske_aloitusvuorot`, `suunta_tekstiksi`, `maarita_reitti`, `laske_pisteet`, `hae_lopputeksti`, `kysy_valinta`, `kysy_nimi`, `kysy_ika`, `lue_teksti`, `tallenna_tulos`, `lue_tulokset`.

### Tiedostot

- Lukeminen: `Intro.txt`, `ohjeet.txt`, `tulokset.txt`
- Kirjoittaminen: `tulokset.txt` (rivin muoto `nimi;ika;reitti;pisteet;vuorot`)

## Bonus

- Pistelaskenta ja parhaiden tulosten lista
- Kahvi ja puhelin lisätoimintoina
- Ikään perustuva vaikeustaso