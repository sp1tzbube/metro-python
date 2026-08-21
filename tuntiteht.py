a = float(input('Anna korkeus(m): '))
b = float(input('Anna leveys(m): '))
c = float(input('Anna kuinka monta neliömetriä seinää voi maalata litralla maalia: '))


print(f"malia tarvitaan noin {round((a*b)/c,2)} l")