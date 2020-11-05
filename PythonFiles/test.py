# import Elem
# import Responces
# import main
# import random
# import sys
# from time import sleep
# --------------------------------------

# def isNumber(value):
# 	correct = True
# 	try:
# 		float(value)
# 	except ValueError:
# 		correct = False

# 	return correct

# def noFloatMessage():
# 	print("We do not accept floats, I'm sorry")

# def numberInput(prompt, Type, noNumMessage = "This is not a number", noFloatMessage = "We do not accept floats"): # add noNumFunc
# 	ask = input(prompt)
# 	if isNumber(ask) == True:
# 		integer = ask.isdigit()
# 		if Type == int:
# 			if integer == True:
# 				return int(ask)
# 			else:
# 				print(noFloatMessage)
# 		elif Type == float:
# 			return float(ask)
# 	else:
# 		print(noNumMessage)
# 		# noNumFunc()


# f = numberInput("oranges: ", int)

# --------------------------------------
# Clyde = Responces.Bot("Clyde", "I am cool")
# User = Responces.User()
# Clyde.Print(Clyde.intro)
# Clyde.pickRandomElement()

# while True:
# 	User.guess()
# 	if int(User.lastGuess) < Clyde.randomElement.number:
# 		Clyde.Print("Too Small\n")
# 	elif int(User.lastGuess) > Clyde.randomElement.number:
# 		Clyde.Print("Too Big\n")
# 	elif int(User.lastGuess) == Clyde.randomElement.number:
# 		Clyde.Print("Perfect\n")
# 		print(User.lastGuess)
# 		print(User.allGuesses)
# 		print(User.guessCount)
		
# 		break

# def Guess():
# 	User.guess()
# 	if (int(User.lastGuess) < Clyde.randomElement.number):
# 		Clyde.Print("Too Small \n")
# 		Guess()
# 	elif (int(User.lastGuess) > Clyde.randomElement.number):
# 		Clyde.Print("Too Big \n")
# 		Guess()
# 	elif int(int(User.lastGuess) == Clyde.randomElement.number):
# 		Clyde.Print("Perfect, \n")
# 		print(User.lastGuess)
# 		print(User.allGuesses)
# 		print(User.guessCount)


# Guess()
	# print(User.lastGuess)
	# print(User.allGuesses)
	# print(User.guessCount)

# def scoreCalculator(x):
# 	score = 0
# 	if x <= 7:
# 		score = ((7 - x + 1) * (7 - x + 2))/2 + 52
# 	else:
# 		score = 59 - x
# 	return score

# print(((7 - 1 + 1) * (7 - 1 + 2))/2)
# print(scoreCalculator(10))
# print(scoreCalculator(9))
# print(scoreCalculator(8))
# print(scoreCalculator(7))
# print(scoreCalculator(6))
# print(scoreCalculator(5))
# print(scoreCalculator(4))
# print(scoreCalculator(3))
# print(scoreCalculator(2))
# print(scoreCalculator(1))