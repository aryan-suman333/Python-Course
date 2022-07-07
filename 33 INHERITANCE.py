class Employee: # base class
	company = "Google"

	def show_details(self):
		print("This is an employee.")

class Programmer(Employee): # derived class
	language = "Python"

	def get_lang(self):
		print("The language is", self.language)

	def show_details(self):
		print("This is an programmer.")

e = Employee()
p = Programmer()

print(e.company)
print(p.company)
e.show_details()
p.show_details()
# programmer waala run hoga agar nhi hota programmer m to employee waala hota
# this is example of single inheritance