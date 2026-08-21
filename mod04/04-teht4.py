year = int(input('Anna vuosi: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print(f"{year} on karkausvuosi")
else:
        print(f"{year} ei ole karkausvuosi")
