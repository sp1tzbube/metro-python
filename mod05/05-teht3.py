y = input('Anna luku: ')

if y != '' :
    max = float(y)
    min = float(y)

while y != '':
    x = float(y)
    if x > max :
        max = x
    elif x < min :
        min = x 
    y = input('Anna luku: ')

print(f"Pienin {min}")
print(f"Suurin {max}")
