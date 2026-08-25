import random 

x = random.randint(1,10)
y = 0

while x != y :
    y = float(input('Anna luku: '))
    if x < y:
        print("Liian suuri arvaus")   
    elif x > y:
        print("Liian pieni arvaus")
    else:
        print("Oikein")  
        break  
    
