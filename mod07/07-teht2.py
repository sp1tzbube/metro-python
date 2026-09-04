import random

luku = 0

def noppa(tahkot):
    luku = random.randint(1, tahkot)
    return luku

tahkot = int(input('Anna  nopan tahkojen määrä: '))

while luku != tahkot:
    luku = noppa(tahkot)
    print(f"Saatiin {luku}")

print(f"Tuli maksimisilmäluku {tahkot}, peli loppuu!")

