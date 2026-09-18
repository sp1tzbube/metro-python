import random

class Inventaario:
    LAADUT = ("hyvä", "keskinkertainen", "huono")   

    def __init__(self, muut_loitsut=None):
        self.loitsut = ["Tulipallo", "Parannus"]
        self.reppu = {}
        
        if muut_loitsut is not None:
            for loitsu in muut_loitsut:
                self.loitsut.append(loitsu)

    def lisaa_tavara(self, nimi):
        laatu = random.choice(self.LAADUT)  
        self.reppu[nimi] = laatu

    def tulosta_reppu(self):
        print("Repun sisältö:")
        for tavara, laatu in self.reppu.items():
            print(f"  -{tavara}: {laatu}")


inventaario = Inventaario(["Salama", "Näkymättömyys"])
print(inventaario.loitsut)

inventaario.lisaa_tavara("Miekka")
inventaario.lisaa_tavara("Kilpi")
inventaario.lisaa_tavara("Taikajuoma")

inventaario.tulosta_reppu()