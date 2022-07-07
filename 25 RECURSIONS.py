def factorial(n):
	if n > 1:
	    return (n * factorial(n-1))
	return 1

print(factorial(4))

def Sum(n):
	if n > 0:
		return (n + Sum(n-1))
	return 0

print(Sum(6))