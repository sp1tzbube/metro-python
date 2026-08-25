i = 1 
y = 0 
while i <= 1000:
    if i%3 == 0 :
        print(i, end='\t')
        y += 1 
        if y == 10 :
            print()
            y = 0
    i += 1    