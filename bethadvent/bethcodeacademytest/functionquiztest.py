def large_power(base, exponent):
    num = base**exponent
    if num > 5000:
        return True
    else:
        return False

#print(large_power(5,6))

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    sum = food_bill + electricity_bill + internet_bill + rent
    if budget < sum:
        return True
    else:
        return False

# print(over_budget(100,20,30,10,40))
# print(over_budget(80,20,30,10,30))

def twice_as_large(num1, num2):
    if num1 > num2*2:
        return True
    else:
        return False
# print(twice_as_large(10,5))
# print(twice_as_large(11,5))

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# print(divisible_by_ten(20))
# print(divisible_by_ten(25))

def not_sum_to_ten(num1, num2):
    sum = num1 + num2
    if sum == 10:
        return False
    else:
        return True
# print(not_sum_to_ten(9,-1))
# print(not_sum_to_ten(9,1))
# print(not_sum_to_ten(5,5))

def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False
# print(in_range(10, 10, 10))
# print(in_range(5, 10, 20))
    
def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False
# print(same_name("Colby", "Colby"))
# print(same_name("Tina", "Amber"))

def always_false(num):
    if num < 0 or num >=0:
        return False
    else:
        return False

# print(always_false(0))
# print(always_false(-1))
# print(always_false(1))

def movie_review(rating):
    if rating <= 5:
        return 'Avoid at all costs!'
    elif rating > 5 and rating < 9:
        return 'This one was fun.'
    else:
        return 'Outstanding!'

# print(movie_review(9))
# print(movie_review(4))
# print(movie_review(6))

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"

# print(max_num(-10, 0, 10))
# print(max_num(-10, 5, -30))
# print(max_num(-5, -10, -10))
# print(max_num(2, 3, 3))

def append_size(lst):
    last = len(lst)
    lst.append(last)
    return lst

# print(append_size([23, 42, 108]))

def append_sum(lst):
    sum = lst[-1] + lst[-2]
    lst.append(sum)
    return lst

# print(append_sum([1,1,2]))

def larger_list(lst1, lst2):
    len1 = len(lst1)
    len2 = len(lst2)
    if len1 >= len2:
        return lst1[-1]
    else:
        return lst2[-1]

# print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

def more_than_n(lst, item, n):
    count = lst.count(item)
    if count > n:
        return True
    else:
        return False

# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

def combine_sort(lst1, lst2):
      lst = lst1 + lst2
      lst.sort()
      return lst

# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

def every_three_nums(start):
    lst = list(range(start, 101, 3))
    return lst

# print(every_three_nums(91))

def remove_middle(lst, start,end):
    del lst[start: end + 1]
    return lst

# print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

def more_frequent_item(lst, item1, item2):
    count1 = lst.count(item1)
    count2 = lst.count(item2)
    
    if count1 >= count2:
        return item1
    else:
        return item2

# print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

def double_index(lst, index):
    if type(index) == int and index <= len(lst)-1:
        lst[index] = lst[index]*2
        return lst
    else:
        return lst 

# print(double_index([3, 8, -10, 12], 2))

def middle_element(lst):
    if len(lst) % 2 == 1:
        return int(lst[int((len(lst)-1)/2)])
    else:
        return int((lst[int((len(lst)/2)-1)]  + lst[int(len(lst)/2)])/2)

print(middle_element([5, 2, -10, -4, 4, 5]))

