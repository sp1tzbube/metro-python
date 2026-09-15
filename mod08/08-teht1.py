kuukaudet = ("kevät", "kesä", "syksy", "talvi")

a = int(input("Anna kuukauden numero: "))

if a in (3, 4, 5):
    print(f"Tämä kuukausi on {kuukaudet[0]}")
elif a in (6, 7, 8):
    print(f"Tämä kuukausi on {kuukaudet[1]}")
elif a in (9, 10, 11):
    print(f"Tämä kuukausi on {kuukaudet[2]}")
elif a in (12, 1, 2):
    print(f"Tämä kuukausi on {kuukaudet[3]}")
else:
    print("Virheellinen kuukauden numero")