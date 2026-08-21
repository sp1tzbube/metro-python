gen,hem = input('Anna sukupuolesi (jos Nainen kirjoita N, jos Mies kirjoita M) ja hemoglobiiniarvo (g/l)\nesim. M 180: ').upper().split()
hem = int(hem)


if gen == 'N':
    if hem < 117:
        print("hemoglobiiniarvo on alhainen")
    elif hem <= 175:
        print("hemoglobiiniarvo on normaali ")
    else:
        print("hemoglobiiniarvo on korkea ")
elif gen == 'M':
    if hem < 134:
        print("hemoglobiiniarvo on alhainen")
    elif hem <= 195:
        print("hemoglobiiniarvo on normaali ")
    else:
        print("hemoglobiiniarvo on korkea ")
else:
    print("virhe")

