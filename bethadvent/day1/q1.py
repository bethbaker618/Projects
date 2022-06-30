txtfile = open('day1.txt')

data = []
for line in txtfile:
    data.append(line.rstrip())

#print(len(data))

depths = [int(i) for i in data]

depthCounter = 0
for i in range(0, (len(depths) - 1)):
    if depths[i] < depths[i + 1]:
        depthCounter += 1

print(depthCounter)