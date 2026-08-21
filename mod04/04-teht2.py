room = input('Anna laivan hyttiluokka (LUX, A, B, C):  ').upper()

if room == 'LUX':
    print("LUX on parvekkeellinen hytti yläkannella.")

elif room == 'A':
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif room == 'B':
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif room == 'C':
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka. anna: LUX, A, B, C")
