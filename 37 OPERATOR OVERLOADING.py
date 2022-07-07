class Number:
	def __init__(self, num):
		self.num = num

	def __add__(self, num2): # operator overloading + ki
		print("Lets add")
		return self.num + num2.num

	def __mul__(self, num2): # operator overloading * ki
		print("Lets multiply")
		return self.num * num2.num

	def __sub__(self, num2): # operator overloading - ki
		print("Lets subtract")
		return self.num - num2.num

	def __truediv__(self, num2): # operator overloading / ki
		print("Lets divide")
		return self.num / num2.num


n1 = Number(4)
n2 = Number(6)

s = n1 + n2
print(s)
s = n1 * n2
print(s)
s = n1 - n2
print(s)
s = n1 / n2
print(s)