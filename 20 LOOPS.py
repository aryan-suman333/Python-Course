i = 0
while i < 10:
	print("Yes " + str(i))
	i += 1

fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
for item in fruits:
	print(item)

for x in range(10):
	print(x)
for x in range(2, 7): # 2 include hoga 7 nhi
	print(x)
for x in range(1, 8, 2): # ek ek chhod k print krega
	print(x)

# for loop with else
for y in range(10):
	print(y)
else:
	print("Done")