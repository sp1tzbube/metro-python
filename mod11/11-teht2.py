class Auto():
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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti): 
        super().__init__(rekisteritunnus,huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        print(f"{self.rekisteritunnus}, {self.huippunopeus} km/h , {self.akkukapasiteetti} kWh")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin):
        super().__init__(rekisteritunnus,huippunopeus)
        self.bensatankin = bensatankin

    def tulosta_tiedot(self):
         print(f"{self.rekisteritunnus}, {self.huippunopeus} km/h , {self.bensatankin} l")


auto1 = Sahkoauto("ABC-15", 180 , 52.5 )
auto2 = Polttomoottoriauto("ACD-123", 165 , 32.3)

auto1.tulosta_tiedot()
auto2.tulosta_tiedot()

auto1.kiihdyta(100)
auto2.kiihdyta(90)

auto1.kulje(3)
auto2.kulje(3)

print(f"\n{auto1.rekisteritunnus} matkamittari: {auto1.kuljettu_matka} km")
print(f"{auto2.rekisteritunnus} matkamittari: {auto2.kuljettu_matka} km")