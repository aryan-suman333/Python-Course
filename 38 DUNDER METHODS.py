class Number:          # __xx__ ese methods ko dunder(double underscore) methods kehte h
	def __init__(self, num):
		self.num = num

	def __str__(self): # direct object print krne k liye
		return f"Decimal Number: {self.num}"

	def __len__(self): # list, vector ki length k liye
		return 1

n = Number(9)
print(n) # __str__ func nhi hota to ye address jesa kuch print krta
print(len(n))