class Hissi():
    def __init__ (self,alin,ylin):
        self.alin = alin
        self.ylin = ylin 
        self.nykyinen = alin

    def siirry_kerrokseen(self, kerros):
        while self.nykyinen != kerros:
            if self.nykyinen < kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen + 1  <= self.ylin:
            self.nykyinen += 1
        else:
            self.nykyinen = self.ylin

        print(f"Nykyinen kerros: {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen - 1  >= self.alin:
            self.nykyinen -= 1
        else:
            self.nykyinen = self.alin

        print(f"Nykyinen kerros: {self.nykyinen}")

class Talo:
    def __init__(self):
        self.hissit = []

    def lisaa_hissi(self, hissi):
        self.hissit.append(hissi)

    def palohalytys(self):
        print("PALOHÄLYTYS! Kaikki hissit siirtyvät pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin)


hissi1 = Hissi(1, 10)
hissi2 = Hissi(1, 6)

talo = Talo()

talo.lisaa_hissi(hissi1)
talo.lisaa_hissi(hissi2)


hissi1.siirry_kerrokseen(8)
print("---")
hissi2.siirry_kerrokseen(5)

print("\n=== PALOHÄLYTYS ALKAA ===\n")
talo.palohalytys()