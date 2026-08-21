a = float(input('Anna leiviskät: '))
b = float(input('Anna naulat: '))
c = float(input('Anna luodit: '))

ans = (((a*20+b)*32)+c)*13.3

kilot = int(ans // 1000)
grammat = round(ans % 1000,2)

print(f"massa on yhteensä {kilot} kg {grammat} g")
