class Auto:
    def __init__(self,rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto("ABC-123",142)

print(f"Auto: {auto1.rekisteritunnus}\n"
      f"Huippunopeus: {auto1.huippunopeus} km/h\n"
      f"Nopeus: {auto1.nopeus} km/h\n"
      f"Matka: {auto1.kuljettu_matka} km"
    )