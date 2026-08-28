numbers = []

num = input('anna luku: ')

while num != '':
    numbers.append(float(num))
    num = input('anna luku: ')

numbers.sort(reverse=True)  

count = min(5, len(numbers))

for i in range(count):
    print(numbers[i], end="\t")

