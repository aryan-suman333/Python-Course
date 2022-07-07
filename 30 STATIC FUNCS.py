class Employee:
	company = "Google"
	salary = 100

	def getSalary(self, sign): # self k alawa dusre arguement bhi de skte
		print(f"Salary of employee({sign}) working in {self.company} is {self.salary}")

	@staticmethod
	def greet():
		print("Good morning, Sir")

harry = Employee()
rajni = Employee()

harry.getSalary("CWH")
rajni.getSalary("RK")
harry.greet() # ye error throw krta agar greet static nhi hota to as greet m humne self
			  # nhi de rkha h, agar static bnane k baad self daale tab bhi error