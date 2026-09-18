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

auto1 = Auto("ABC-123", 142)

print(f"Auto: {auto1.rekisteritunnus}\n"
      f"Huippunopeus: {auto1.huippunopeus} km/h\n"
      f"Nopeus: {auto1.nopeus} km/h\n"
      f"Matka: {auto1.kuljettu_matka} km")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print("Nopeus kiihdytysten jälkeen:", auto1.nopeus, "km/h")

auto1.kiihdyta(-200)
print("Nopeus hätäjarrutuksen jälkeen:", auto1.nopeus, "km/h")

