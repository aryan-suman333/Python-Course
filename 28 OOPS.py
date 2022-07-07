class Number:
	def sum(self): # self basically this h cpp waala (object ko point krta h) prr hum
				   # self ki jgh kuch bhi use kr skte h(krna nhi h but)
		return self.a + self.b

num = Number() # object bnaya
num.a = 12
num.b = 24
s = num.sum()
print(s)

class RailwayForm:
	formType = "RailwayForm" # formtype saare objects ka same hi rhega kisi particular
							 # object ka hum obj.formtype = "" kr k change kr skte h
	def printData(self):
		print(f"Name is {self.name}")
		print(f"Train is {self.train}")

harrys_application = RailwayForm()
harrys_application.name = "Harry"
harrys_application.train = "Rajdhani Express"
harrys_application.printData()