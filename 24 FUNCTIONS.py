def percent(marks):
	return ((marks[0] + marks[1] + marks[2] + marks[3])/400) * 100

marks1 = [45, 78, 86, 77]
print(percent(marks1))

marks2 = [75, 98, 88, 78]
print(percent(marks2))

def Sum(num1, num2):
	return num1 + num2

print(Sum(3, 6))

def greet(name = "Stranger"):
	print("Good day, " + name)

greet("Aryan")
greet()