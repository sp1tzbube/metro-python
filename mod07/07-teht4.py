def laske(luvut):
    suma = 0
    for luku in luvut:
        suma += luku
    return suma


s = []
a = int(input('Anna listan koko: '))

for i in range(a):
    b = int(input('Anna luku: '))
    s.append(b)

tulos = laske(s)
print(f"Summa on {tulos}")