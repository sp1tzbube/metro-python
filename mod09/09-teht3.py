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

auto1 = Auto("ABC-123",142)
auto1.kiihdyta(60) 
auto1.kulje(1.5)

print(f"\nNopeus: {auto1.nopeus} km/h ")
print(f"Kuljettu matka: {auto1.kuljettu_matka} km")



