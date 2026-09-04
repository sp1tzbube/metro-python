def dele(l1):
    l2 = []
    for i in l1:
        if i % 2 == 0:
            l2.append(i)
    return l2


lista_1 = []

a = int(input('Anna listan koko: '))

for i in range(a):
    b = int(input('Anna luku: '))
    lista_1.append(b)

lista_2 = dele(lista_1)

print(f"Alkuperäinen lista: {lista_1}")
print(f"Karsittu lista (vain parilliset): {lista_2}")