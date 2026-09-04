import random

luku = 0

def noppa():
    luku = random.randint(1, 6)
    return luku

while luku != 6:
    luku = noppa()
    print(f"Saatiin {luku}")

print("Tuli kuutonen, peli loppuu!")

