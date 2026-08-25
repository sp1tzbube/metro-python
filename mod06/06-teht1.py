import random 

a = int (input('Anna arpakuutioiden lukumäärä: '))
s = 0

for i in range(a):
    s += random.randint(1,6)

print(f"Summa on {s}")    