name_1 = "python"
pasw_1 = "rules"
i = 0 

while i < 5 :
    name = input('Anna  käyttäjätunnus: ')
    pasw = input('Anna salasana: ')
    if name == name_1 and pasw == pasw_1 :
        print("Tervetuloa!")
        break
    i += 1
else:   
    print("Pääsy evätty")