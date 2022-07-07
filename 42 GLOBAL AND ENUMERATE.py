a = 54
def func1():
	global a # yaha ye ni likhte to local a = 8 hota global 54 hi rehta
	a = 8
	print(a)

func1()
print(a)

list1 = [3, 53, False, 6.2, "Harry"]

for i, item in enumerate(list1): # yaha p index ya i jo bhi h usko pehle likhenge
	print(item , 'index  =', i)

# ***list comprehensions***

a = [3, 5, 7, 9, 11, 13, 15, 17, 19]

# b = []
# for item in a:
# 	if item > 9:
# 		b.append(item)

b = [i for i in a if i > 9] # dict or sets m bhi use kr skte h
print(b)

l = [1, 2, 4, 3, 1, 3, 2]
s = {i for i in l}
print(s)