import random 

koodi_1 = ""
koodi_2 = ""

koodi_1 += str(random.randint(0,9))
koodi_1 += str(random.randint(0,9))
koodi_1 += str(random.randint(0,9))

koodi_2 += str(random.randint(1,6))
koodi_2 += str(random.randint(1,6))
koodi_2 += str(random.randint(1,6))
koodi_2 += str(random.randint(1,6))

"""
#voi olla myös 

for i in range(3):
    koodi_1 += str(random.randint(0,9)

for i in range(4):
    koodi_2 += str(random.randint(1,6)
"""

print(f"Kolminumeroinen koodi {koodi_1}")
print(f"Nelinumeroinen koodi {koodi_2}")


