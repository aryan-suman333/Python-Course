class Person:                      # this is an exapmle of multilevel inheritance
	country = "India"
	def take_breath(self):
		print("I am breathing...")

class Employee(Person):
	company = "Honda"
	def take_breath(self):
		super().take_breath()  # jab bhi take_breath run hoga to iski parent class
							   # ka takebreth bhi run hoga, agar base class ka takebreth
							   # koi arguement leta hota to vo hum yaha p dedete
		print("I am an employee and i am luckily breathing...")

class Programmer(Employee):
	company = "Fiverr"
	def take_breath(self):
		super().take_breath() # basically parent class(sirf ek level upar waali) se koi 
							  # function, constructor run kraane k liye use hota h super
		print("I am an programmer and i am breathing++...")

p = Person()
p.take_breath()

e = Employee()
e.take_breath()

pr = Programmer() 
pr.take_breath()