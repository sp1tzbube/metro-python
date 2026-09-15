def check_name(nimet, uusi):
    if uusi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")

nimet = set()

while True:
    name = input("Anna nimi: ")
    if name == "":
        break
    check_name(nimet, name)
    nimet.add(name)

print("\nSyötetyt nimet:")
for nimi in nimet:
    print(nimi)