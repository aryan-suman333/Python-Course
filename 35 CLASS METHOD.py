class Employee:
	company = "Camel"
	salary = 100
	location = "Delhi"

	@classmethod
	def change_salary(cls, sal): # cls use hoga class k liye
		cls.salary = sal
	# is function ka obj se koi lena dena nhi h sirf class attribute ko change kr rha h
	# isliye class method(vrna self dena pdta) or self.salary se change krte to obj ki 
	# salary change hoti class ki nhi
	

	# def change_salary(self, sal): # ese bhi kr skte h prr kyu krna
	# 	self.__class__.salary = sal


e = Employee()
print(e.salary)
e.change_salary(200) # yaha Employee.change_salary likh k bhi kr skte
print(e.salary)
print(Employee.salary) # class attribute hi change ho gya