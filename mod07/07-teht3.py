def litra(gallona):
    litraa = gallona * 3.785
    return litraa

gallona = 1
while gallona > 0:
    gallona = float(input('Anna gallonamäärä(negatiivinen lopettaa): '))


    if gallona > 0:
        l = litra(gallona)
        print(f"{gallona} gallonaa on {l:.2f} litraa")
    else:
        print("Lopetetaan")