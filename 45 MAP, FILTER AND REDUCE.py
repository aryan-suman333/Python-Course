from functools import reduce
def square(num):
	return num*num

l1 = [1, 2, 4]

# method 1
# l2 = []
# for item in  l1:
# 	l2.append(square(item))
# print(l2)

# method 2
print(map(square, l1))
print(list(map(square, l1)))

def greater(num):
	if num > 5:
		return True
	else:
		return False

lesser = lambda num : num<5
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(filter(greater, l3))
print(list(filter(greater, l3))) # yaha function or lambda func dono use kr skte h
print(list(filter(lesser, l3)))

add = lambda a, b : a+b
mul = lambda a, b : a*b

value = reduce(add, l3)
print(value)
value = reduce(mul, l3)
print(value)