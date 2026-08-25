import random 

n = int(input('Anna pisteiden määrä: '))
i = 0 
nn = 0


while i < n :
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2 < 1:
        nn += 1
    i += 1

print(f"Pii likiarvo {4*nn/n}")