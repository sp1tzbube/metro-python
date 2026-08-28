a =  int(input('anna luku: '))
p = True

if a < 2:
    p = False
else:
        
    for i in range(2,a):
        if a % i == 0:
            p = False
            break

if p == False:
    print("luku ei ole alkuluku")     

else: 
    print("luku on alkuluku")        
