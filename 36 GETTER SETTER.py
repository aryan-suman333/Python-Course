class Employee:
	company = "MLF"
	salary = 4500
	salary_bonus = 500

			  # isko define as a func kiya h but ye salary or company jese ek class
	@property # attribute(property) h @prperty ko getter bhi bolte h
	def total_salary(self):
		return self.salary + self.salary_bonus

	@total_salary.setter # isko setter bolte h
	def total_salary(self, val):
		self.salary_bonus = val - self.salary
	# ye isliye kr rhe h kyoki agar humne kahi p total_salary ko change kiya to
	# actually m salary ya salary_bonus m se kuch ek change krna hoga

e = Employee()
print(e.total_salary)
e.total_salary = 5800 # is line m setter run hoga
print(e.total_salary)
print(e.salary_bonus)