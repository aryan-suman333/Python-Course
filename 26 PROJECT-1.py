import random

def game_win(comp, you):
	if comp == you:
		return None

	elif comp == 's':
		if you == 'w':
			return False
		elif you == 'g':
			return True
	elif comp == 'w':
		if you == 'g':
			return False
		elif you == 's':
			return True
	elif comp == 'g':
		if you == 's':
			return False
		elif you == 'w':
			return True
		


comp = print("Computer Turn: Snake(s), Water(w) or Gun(g)?\n")
random_num = random.randint(1, 3) # 1 2 3 m se ek aata rhega
if random_num == 1:
	comp = 's'
elif(random_num == 2):
	comp = 'w'
else:
	comp = 'g'

you = input("Your Turn: Snake(s), Water(w) or Gun(g)?\n")

print("Computer chose " + comp, "and You chose " + you)

a = game_win(comp, you)
if a == None:
	print("The game is tie!\n")
elif a:
	print("You win!\n")
else:
	print("You loose!\n")