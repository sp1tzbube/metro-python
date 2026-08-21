a = int(input('Anna korkeus(m): '))
b = int(input('Anna leveys(m): '))
c = int(input('Anna kuinka monta neliömetriä seinää voi maalata litralla maalia: '))


print(f"malia tarvitaan noin {round((a*b)/c,2)} l")