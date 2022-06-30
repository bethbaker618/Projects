txtfile = open('diagnostic.txt')

data = []
for line in txtfile:
    data.append(line.rstrip())

epsilon = ''
gamma = ''
str_length = len(data[0])
list_length = len(data)
for i in range(str_length):
    count_0 = 0
    count_1 = 0
    for j in range(list_length):
        if data[j][i] == '0':
            count_0 += 1
        else:
            count_1 += 1
    if count_0 < count_1:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon,2)

power_consumption = gamma_decimal * epsilon_decimal
print(power_consumption)
    

            

    






