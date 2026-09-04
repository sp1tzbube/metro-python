import math

def pizza(halkaisija, hinta):
    sade_m = (halkaisija / 100) / 2
    pinta_ala = math.pi * sade_m ** 2 
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta 


d1, h1 = input('Anna pizza 1 halkaisija (cm) ja hinta (€), esim. "30 12.5": ').split()
d1 = float(d1)
h1 = float(h1)

d2, h2 = input('Anna pizza 2 halkaisija (cm) ja hinta (€), esim. "24 13": ').split()
d2 = float(d2)
h2 = float(h2)


yksikkohinta1 = pizza(d1,h1)
yksikkohinta2 = pizza(d2,h2)

print(f"Pizza 1 yksikköhinta: {yksikkohinta1:.2f} €/m2")
print(f"Pizza 2 yksikköhinta: {yksikkohinta2:.2f} €/m2")

if yksikkohinta1 < yksikkohinta2:
    print("Pizza 1 on edullisempi eli antaa paremman vastineen rahalle")

elif yksikkohinta1 > yksikkohinta2:
    print("Pizza 2 on edullisempi eli antaa paremman vastineen rahalle")
 

else: print("Molemmat pizzat maksavat saman verran neliömetriltä")



