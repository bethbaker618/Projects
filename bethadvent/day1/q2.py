txtfile = open('day1.txt')

data = []
for line in txtfile:
    data.append(line.rstrip())

#print(len(data))

depths = [int(i) for i in data]

count = 0
for i in range(0, (len(depths) - 3)):
    first_sum = depths[i] + depths[i + 1] + depths[i + 2]
    second_sum = depths[i + 1] + depths[i + 2] + depths[i + 3]
    if first_sum < second_sum:
        count += 1 
print(count)