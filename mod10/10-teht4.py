import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        uusi_nopeus = self.nopeus + muutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, aika):
        self.kuljettu_matka += self.nopeus * aika


class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus, autojen_lista):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus = pituus
        self.autojen_lista = autojen_lista

    def tunti_kuluu(self):
        for auto in self.autojen_lista:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n=== {self.kilpailun_nimi} - tilanne ===")
        print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
        for auto in self.autojen_lista:
            print(f"{auto.rekisteritunnus:<18}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.kuljettu_matka:<10.1f}")

    def kilpailu_ohi(self):
        for auto in self.autojen_lista:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunteja_kulunut = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunteja_kulunut += 1

    if tunteja_kulunut % 10 == 0:
        kilpailu.tulosta_tilanne()

print("\nKilpailu on ohi!")
kilpailu.tulosta_tilanne()
print(f"\nKilpailu kesti {tunteja_kulunut} tuntia.")