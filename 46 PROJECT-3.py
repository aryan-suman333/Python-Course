class Library:
	def __init__(self, listOfBooks):
		self.books = listOfBooks
		
	def display(self):
		print("The books present in this library are: ")
		for book in self.books:
			print('\t' + book)

	def borrowBook(self, bookName):
		if bookName in self.books:
			print(f"You have been issued '{bookName}'. Please keep it safe.")
			self.books.remove(bookName)
			return True
		else:
			print("Sorry, this book is either not available or has already been issued to someone else.")
			return False

	def returnBook(self, bookName):
		self.books.append(bookName)
		print("Thanks for returning or adding this book.")
		
class Student:
	def requestBook(self):
		self.book = input("Enter name of the book, you want to borrow: ")
		return self.book

	def returnBook(self):
		self.book = input("Enter name of the book, you want to return or add: ")
		return self.book

if __name__ == '__main__':
	centralLibrary = Library(["algo", "django", "let us see", "python"])
	student = Student()

	while True:
		welcomeMsg = '''\nWelcome to central library!
		Please choose a option: 
		1. Display available books
		2. Request a book
		3. Return or add a book
		4. Exit'''

		print(welcomeMsg)

		a = int(input("Enter a choice: "))
		if a == 1:
			centralLibrary.display()
		elif a == 2:
			centralLibrary.borrowBook(student.requestBook())
		elif a == 3:
			centralLibrary.returnBook(student.returnBook())
		elif a == 4:
			print("Thank You!")
			exit()
		else:
			print("Invalid choice")

		