lentot = {"EFHK": "Viivi",
          "EFDD": "Ahmed",
          "RTLN": "Pekka"}

while True:
    a = input("Mitä sinä haluat tehdä [1-3]:\n"
               " 1. uuden lentoaseman syöttäminen\n"
               " 2. haku ICAO-koodilla\n"
               " 3. lopeta\n")

    if a == "1":
        koodi = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentot[koodi] = nimi
    elif a == "2":
        koodi = input("Anna ICAO-koodi: ")
        if koodi in lentot:
            print(lentot[koodi])
        else:
            print("Koodia ei löytynyt")
    elif a == "3":
        break
    else:
        print("Virheellinen valinta")