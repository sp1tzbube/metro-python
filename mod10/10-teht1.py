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

h = Hissi(1, 10)
h.siirry_kerrokseen(6)
print("-------------------------------------")
h.siirry_kerrokseen(1)