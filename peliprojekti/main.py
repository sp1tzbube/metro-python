import random
name = input('Anna nimesi: ')
age = int(input('Anna ikäsi: '))

if age < 12: 
    print("Olet alaikäinen, peli sulkeutuu.")
    exit()
else:
    print(f"Tervetuloa, {name}!")

w = ''
while w != 'lopeta':
    print("\n--------- Päävalikko ---------")
    print("Komennot: ")
    w = input('Anna komento: koe, tunti, ope, koulu, pisteet, arvonta, lopeta: ')
    print("\n--------- ---------  ---------")

    if w == 'koe':
        print("--> Koe tulee ensi viikolla ")
    
    elif w == 'tunti':
        print("--> Nyt on Python-tunti")

    elif w == 'ope':
        print("--> Sinun opesi ovat Haavisto Aino ja Heinonen Ava")

    elif w == 'koulu':
        print("--> Sinun koulu on Metropolia")

    elif w == 'pisteet':
        pisteet = random.randint(0, 100)
        print(f"--> Sinun pisteesi: {pisteet}/100")
 
    elif w == 'arvonta':
        luku = random.randint(1, 5)
        print(f"--> Onnenlukusi on: {luku}")
   
    elif w == 'lopeta':
        print("--> Nähdään taas !")

    
    else: print("Virhe!")
         

    
print(f"Sun nimesi on {name} ,ja ikäsi on {age}")
