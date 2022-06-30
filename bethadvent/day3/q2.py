txtfile = open('diagnostic.txt')

data = []
for line in txtfile:
    data.append(line.rstrip())


data1 = data.copy()
data2 = data.copy()

i = 0
while len(data1) > 1:
    zeros = 0
    ones = 0

    for string in data1:
        if string[i] == '0':
            zeros += 1
        else:
            ones += 1 


    if zeros > ones:
        data1 = [string for string in data1 if string[i] == '0']
       
    else:
        data1 = [string for string in data1 if string[i] == '1']
    
    i += 1 

print(data1)

i = 0
while len(data2) > 1:
    zeros = 0
    ones = 0

    for string in data2:
        if string[i] == '0':
            zeros += 1
        else:
            ones += 1 

    if zeros > ones:
        data2 = [string for string in data2 if string[i] == '1']
    else:
        data2 = [string for string in data2 if string[i] == '0']
    
    i += 1 

print(data2)

oxygen_decimal = int(data1[0], 2)
carbon_decimal = int(data2[0], 2)

print(oxygen_decimal)
print(carbon_decimal)
support_rating = oxygen_decimal*carbon_decimal
print(support_rating)
 


