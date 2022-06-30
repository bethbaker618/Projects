txtfile = open('text.txt')

data = []
for line in txtfile:
    data.append(line.rstrip())
#print(data)

split_data = [word for line in data for word in line.split()]
words = split_data[::2]
#print(words)

numbers = list(map(int, split_data[1::2]))
print(numbers)

horizontal = 0
depth = 0
index = 0
for i in words:
    if i == 'forward':
        horizontal = horizontal + numbers[index]
    elif i == 'down':
        depth = depth + numbers[index]
    else:
        depth = depth - numbers[index]
    index += 1
solution = horizontal*depth

print(solution)

 