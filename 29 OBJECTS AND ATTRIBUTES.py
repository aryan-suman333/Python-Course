class Employee:
	company = "Google" # class attribute
	salary = 100
	def getSalary(self):
		print(f"Salary of employee working in {self.company} is {self.salary}")

harry = Employee()
rajni = Employee()
print(harry.company)
print(rajni.company)

harry.company = "Youtube"
print(harry.company)
print(rajni.company)

Employee.company = "Youtube"
print(harry.company)
print(rajni.company)

harry.salary = 300 # age object attribute, salary both class and object attribute
harry.age = 30
rajni.age = 40

print(harry.salary)
print(rajni.salary)
print(harry.age)
print(rajni.age)
harry.getSalary()
rajni.getSalary()