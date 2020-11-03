# import Elem
import Responces
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
Clyde = Responces.Bot("Clyde", "I am cool")
Clyde.Print(Clyde.intro)
Clyde.pickRandomElement()
