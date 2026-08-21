fish = int(input('Anna kuhan pituus senttimetreinä: '))

if fish < 37:
    print(f"Kuha on alamittainen, palauta kala takaisin järveen. Mitasta puuttuu {37-fish} cm")

else:
    print("Kuha on hyvän mittainen, voit ottaa kalan")