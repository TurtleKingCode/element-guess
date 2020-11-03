import Elem
import random
import sys
from time import sleep

# Setting up Functions and Objects
class Bot:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.intro = "Hi, my name is " + self.name + "\n\n" + self.description + "."
	randomElement = 0
	
	def pickRandomElement(self):
		Bot.randomElement = random.choice(Elem.Elements)
		if (Bot.randomElement.number == 0):
			Bot.pickRandomElement(self)

	def askName(self):
		return "Anyways, what " + System.generateRandomMessage(System.nameAdjs.first) + " name do you want me to call you?"

	def Print(self,words, sleep_time=0.01):
		for char in words:
			sleep(sleep_time)
			sys.stdout.write(char)
			sys.stdout.flush()


class System:
	def printRandomMessage(messages):
		print(random.choice(messages))
	def generateRandomMessage(messages):
		return random.choice(messages)
	class nameAdjs:
		first = ["cool", "awesome"]
		second = ["splendiferous", "fantastical", "outstanding", "awesome", "fantabulous", "radical"]
			# self.chooseFirst = random.choice(self.first)
			# self.chooseSecond = random.choice(self.second)


# System = System()
# Calling Functions and Objects
# nameAdjs = nameAdjs()
# guessPhrases = guessPhrases()
# print(System.generateRandomMessage(System.nameAdjs().first))
# print(System.nameAdjs().first)
# User = User()
class User:
	phrases = ["I'm guessing: ", "I'm feeling like: ", "I'll say the number is: ", "Is the number: ", "I think the number could be: ", "How about: "]
	allGuesses = []
	guessCount = 0
	lastGuess = 0
	class info:
		def __init__(self):
			self.name = str(input("My " + System.generateRandomMessage(System.nameAdjs.second) + " name is: "))
	def guess(self):
		guessInput = input(System.generateRandomMessage(User.phrases))
		User.allGuesses.append(guessInput)
		User.guessCount += 1
		User.lastGuess = guessInput