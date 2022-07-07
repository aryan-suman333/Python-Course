class Calculator:
	def __init__(self, num):
		self.number = num

	def square(self):
		print(f"Square of {self.number} is {self.number **2}")

	def cube(self):
		print(f"Cube of {self.number} is {self.number **3}")

	def squareRoot(self):
		print(f"Square root of {self.number} is {self.number **0.5}")

a = Calculator(4)
a.square()
a.cube()
a.squareRoot()

class Train:
	def __init__(self, name, fare, seats):
		self.name = name
		self.fare = fare
		self.seats = seats

	def getStatus(self):
		print(f"The name of the train is {self.name}")
		print(f"The no. of seats available in this train is {self.seats}")

	def fareInfo(self):
		print(f"The fare of this train is Rs {self.fare}")

	def bookTicket(self):
		if self.seats > 0:
			print("Your ticket has been booked.")
			print("Your seat no. is", self.seats)
			self.seats -= 1
		else:
			print("Sorry, the train is full.")

intercity = Train("Intercity Express", 90, 300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()