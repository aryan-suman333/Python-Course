class Employee:
	company = "Google"

	def __init__(self, salary, age, subunit): # constructor ka naam __init__ hi hota h,
											  # self isme hona chahiye must
		print("Employee is created.")
		self.age = age
		self.salary = salary
		self.subunit = subunit

	def getDetails(self):
		print(f'''Salary, age and subunit of employee working in {self.company} is {self.salary}, {self.age} and {self.subunit}.''')

	@staticmethod
	def greet():
		print("Good morning, Sir")

harry = Employee(100, 25, "Youtube")
harry.greet()
harry.getDetails()

rajni = Employee(200, 30, "Gmeet")
rajni.greet()
rajni.getDetails()