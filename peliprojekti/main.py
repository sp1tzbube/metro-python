import random

reppu_lista = []

def koe():
    print("--> Koe tulee ensi viikolla ")

def tunti():
    print("--> Nyt on Python-tunti")

def ope():
    print("--> Sinun opesi ovat Haavisto Aino ja Heinonen Ava")

def koulu():
    print("--> Sinun koulu on Metropolia")

def pisteet():
    pisteet = random.randint(0, 100)
    print(f"--> Sinun pisteesi: {pisteet}/100")

def arvonta():
    luku = random.randint(1, 5)
    print(f"--> Onnenlukusi on: {luku}")

def lisaa_esine():
    vastaus = input('haluatko lisätä esineen reppuun? (joo/ei): ').lower()

    if vastaus == 'joo':
        item = input('Mitä haluat laittaa reppuun: ')
        reppu_lista.append(item)
        print(f"--> {item} lisättiin reppuun!")
    else: 
        print('Okei, ensi kerralla')

def nayta_reppu():
    if len(reppu_lista) == 0:
        print("--> Reppusi on tyhjä")
    else: 
        print("Reppusi sisältö: ")
        for item in reppu_lista:
            print(f"  - {item}")

def lopeta():
    print("--> Nähdään taas !")



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
    w = input('Anna komento: koe, tunti, ope, koulu, pisteet, arvonta, lisätä, reppu, lopeta: ')
    print("\n--------- ---------  ---------")

    if w == 'koe':
        koe()
    
    elif w == 'tunti':
        tunti()

    elif w == 'ope':
        ope()

    elif w == 'koulu':
        koulu()

    elif w == 'pisteet':
        pisteet()
 
    elif w == 'arvonta':
        arvonta()

    elif w == 'lisätä':
        lisaa_esine()
    
    elif w == 'reppu':
        nayta_reppu()
   
    elif w == 'lopeta':
        lopeta()

    else: print("Virhe!")
    
         

    
print(f"Sun nimesi on {name}, ja ikäsi on {age}")
