**Pelinimi on "Etsi väsynyt tutori"**

**Dmytro Orlov**


# Etsi väsynyt tutori

Komentorivillä pelattava peli, joka sijoittuu Helsingin ja Espoon M1-metrolinjalle (Vuosaari – Kivenlahti, 27 asemaa).

## Tarina ja tavoite

Perjantai-iltana tutorisi nukahti M1-metroon eikä vastaa puhelimeen. Metro sulkeutuu keskiyöllä.

**Tavoite: löydä tutori ennen kuin vuorot loppuvat.**
Vuorot ovat aikaa keskiyöhön. Liikkuminen, etsiminen, vartijalta kysyminen ja soittaminen maksavat yhden vuoron.

Peli sopii myös alaikäisille (K12): tarina on rauhallinen, eikä siinä ole väkivaltaa eikä päihteitä.

## Näin peliä pelataan

1. Anna nimesi ja ikäsi. Alle 13-vuotias saa 30 vuoroa, muut 24.
2. Pelaaja ja tutori arvotaan eri asemille.
3. Valitse valikosta, mitä teet: liiku, etsi, kysy vartijalta, soita tai osta kahvi.
4. Etsintä antaa vihjeen: kuuma, haalea tai kylmä (etäisyyden mukaan).
5. Löydät tutorin, kun etsit samalta asemalta, jolla hän nukkuu.

## Toiminnot pelissä

| Toiminto | Mitä tapahtuu |
|---|---|
| Eteenpäin / taaksepäin | Siirryt viereiselle asemalle. Matkalla voi sattua jotain. |
| Etsi | Tarkistat aseman. Tutori löytyy tai saat vihjeen. |
| Kysy vartijalta | Kertoo suunnan ja arvion etäisyydestä (vain asemilla, joilla on vartija). |
| Soita tutorille | Soittoääni kertoo, onko tutori lähellä. Puheluja on 2. |
| Osta kahvi | Maksaa 1 vuoron ja antaa 3 (vain asemilla, joilla on kahvila). |

## Neljä reittiä voittoon

| Reitti | Miten | Bonus |
|---|---|---|
| Yksin tutkijana | Vain etsitään ja tulkitaan vihjeitä | +50 |
| Vartijan avulla | Käytetään järjestyksenvalvojaa | +20 |
| Puhelun avulla | Käytetään puhelinta | +20 |
| Tiimityö | Käytetään sekä vartijaa että puhelinta | +30 |

Jokaisella reitillä on oma lopputeksti. Jos metro sulkeutuu ennen kuin tutori löytyy, peli päättyy häviöön.

**Pisteet = 10 × jäljellä olevat vuorot + reittibonus.**

Tulokset tallentuvat tiedostoon `tulokset.txt`, ja päävalikosta näkee viisi parasta.

## Kestävä kehitys

Peli liittyy YK:n tavoitteisiin **11 (kestävät kaupungit ja yhteisöt)** ja **13 (ilmastoteot)**:

- Koko peli tapahtuu joukkoliikenteessä, ja lopussa tutori ja pelaaja matkustavat kotiin metrolla.
- Matkalla näkyy "Tiesitkö?"-tietoja joukkoliikenteestä, kävelystä ja kierrätyksestä.
- Kahvi juodaan omaan termosmukiin, joten kertakäyttökuppeja ei tarvita.

## Ohjelman rakenne

- **Pelaaja**: nimi, ikä, sijainti, vuorot ja käytetyt apukeinot.
- **Peli**: yksi pelikerta, sisältää pelaajan, tutorin sijainnin ja pääsilmukan `aja()`.
- **Tiedostot**: luetaan `intro.txt`, `ohjeet.txt` ja `tulokset.txt`. Kirjoitetaan `tulokset.txt` (rivi: `nimi;ika;reitti;pisteet;vuorot`).

## Bonus

- Pistelaskenta ja viiden parhaan lista
- Kahvi ja puhelin lisätoimintoina
- Ikään perustuva vaikeustaso