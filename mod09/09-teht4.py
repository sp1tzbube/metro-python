import random

class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 2000

    def kiihdyta(self, muutos):
        uusi_nopeus = self.nopeus + muutos 

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus
    
    def kulje(self,aika):
        self.kuljettu_matka += self.nopeus * aika

        if self.kuljettu_matka == 10000:
            lopeta = True 

autot = []

for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

lopeta = False

while not lopeta:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            lopeta = True
            voittaja = auto
            break
     
print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<18}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.kuljettu_matka:<10.1f}")

print("------------------------------------------------------")
print(f"Voitaja on {voittaja.rekisteritunnus}")