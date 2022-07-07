n = int(input("Enter the number: "))

for i in range(n):
	print("*" * (i+1))

for i in range(n):
	print(" " * (n-i-1), end="") # end="" ye new line print nhi hone deta
	print("*" * (2*i+1), end="")
	print(" " * (n-i-1))

def pattern(n):
	for i in range(n):
		print("*" * (n-i))

pattern(n)