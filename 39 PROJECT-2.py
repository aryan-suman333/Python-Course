import random
randNum = random.randint(1, 100) # 1 and 100 included

user = None # initialize
guesses = 0

while user != randNum:
	user = int(input("Enter your guess: "))
	if user == randNum:
		print("You guessed it right! ")
	elif user > randNum:
		print("Your guess is more than the number. ")
	else:
		print("Your guess is less than the number. ")
	guesses += 1

print("Guesses:", guesses)