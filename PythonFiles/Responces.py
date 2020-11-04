import Elem
import random
import sys
from time import sleep

# Setting up Functions and Objects
class Bot:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.intro = "Hi, my name is " + self.name + " 👋👋👋\n\n" + self.description + "."
	randomElement = 0
	
	def pickRandomElement(self):
		Bot.randomElement = random.choice(Elem.Elements)
		if (Bot.randomElement.number == 0):
			Bot.pickRandomElement(self)

	def askName(self):
		return "Anyways, what " + System.generateRandomMessage(System.nameAdjs.first) + " name do you want me to call you?"

	def Print(self, words, sleep_time=0.01):
		for char in (words + "\n"):
			sleep(sleep_time)
			sys.stdout.write(char)
			sys.stdout.flush()

	def Game(self, bot, user):
		reactorResults = user.guessData.guessReactor(bot, user)
		if (int(reactorResults.value) < bot.randomElement.number):
			bot.Print("Too Small")
			bot.Game(bot, user)
		elif (int(reactorResults.value) > bot.randomElement.number):
			bot.Print("Too Big")
			bot.Game(bot, user)
		elif (int(reactorResults.value) == bot.randomElement.number):
			bot.Print("Perfect")
	class guessResponces:
		def __init__ (self, bot, element):
			self.tooLow = ["Too Small", "Not High Enough", "Not Heavy Enough", element.name + " Doesn't Have Enough Protons", "Your Atomic Number Needs to Get Bigger", "My Element is Heavier", bot.name + " Wants More More MORE!!!!", "Directions: 👆"]
			self.tooHigh = ["Too Big", "Not Low Enough", "Not Light Enough", element.name + " Has Too Many Protons", "Your Atomic Number Needs to Get Smaller", "My Element is Lighter", + bot.name + " Says You're Too Far Ahed", "Direction: 👇"]
			self.perfect = ["Perfect", "You Got It", "Clyde is Proud of You", "You Got is Right, " + element.name + " Was the Element I Had In Mind", "That's Just the Right # of Protons", bot.name + " Is Very Proud of You. For Guessing the Number", "You Just Made " + bot.name + " Proud.  UwU", "👍👍👍"]



class System:
	def printRandomMessage(messages):
		print(random.choice(messages))
	def generateRandomMessage(messages):
		return random.choice(messages)
	class nameAdjs:
		first = ["cool", "awesome"]
		second = ["splendiferous", "fantastical", "outstanding", "awesome", "fantabulous", "radical"]
	def isNumber(value):
		global number
		number = True
		try:
			float(value)
		except ValueError:
			number = False
		return number
	def isInt(value):
		if System.isNumber(value) == True:
			if str(value).isdigit() == True:
				return True
			else:
				return False

class User:
	phrases = ["I'm guessing: ", "I'm feeling like: ", "I'll say the number is: ", "Is the number: ", "I think the number could be: ", "How about: "]
	allGuesses = []
	# allGuesses_nonRepeat
	guessCount = 0
	guessInput = 0
	class guessData:
		class lastGuess:
			value = 0
			def element():
				reNewedElement = Elem.Elements[int(User.guessData.lastGuess.value)].number
				return reNewedElement
		class repeat:
			guessCount = 0
			allGuesses = []
		class noRepeat:
			guessCount = 0
			allGuesses = []
		class results:
			def __init__(self, value, Num, intBool, repeated):
				self.value = value
				self.Num = Num
				self.intBool = intBool
				self.repeated = repeated

		def guessReactor(bot, user):
			guess = input(System.generateRandomMessage(User.phrases))
			# guess = user.guess()
			guessTable = user.guessData.repeat.allGuesses
			Num = System.isNumber(guess)
			intBool = System.isInt(guess)
			global repeated

			if Num == False:
				print("This is not a number... Try again")
				bot.Game(bot, user)
			else:
				if intBool == False:
					print("This is a float, we do not accept floats")
					bot.Game(bot, user)
				else:
					repeated = (int(guess) in guessTable)
					if repeated == True:
						User.guessData.lastGuess.value = int(guess)
						User.guessData.repeat.guessCount += 1
						User.guessData.repeat.allGuesses.append(User.guessData.lastGuess.value)
						print(User.guessData.repeat.guessCount)
						print(User.guessData.repeat.allGuesses)
						print(User.guessData.lastGuess.value)
					else:
						User.guessData.lastGuess.value = int(guess)
						User.guessData.repeat.guessCount += 1
						User.guessData.repeat.allGuesses.append(User.guessData.lastGuess.value)
						User.guessData.noRepeat.guessCount += 1
						User.guessData.noRepeat.allGuesses.append(User.guessData.lastGuess.value)
						print(str(User.guessData.noRepeat.guessCount) + " no repeats")
						print(str(User.guessData.noRepeat.allGuesses) + " no repeats")
						print(str(User.guessData.repeat.guessCount) + " repeats")
						print(str(User.guessData.repeat.allGuesses) + " repeats")
						print(repeated)
			return User.guessData.results(guess, Num, intBool, User.guessData.guessReactor)

	class info:
		def __init__(self):
			self.name = str(input("My " + System.generateRandomMessage(System.nameAdjs.second) + " name is: "))
	def guess(self):
		oranges = 345
		oranges += 1
		# User.guessData.examineGuess()
		# return guessInput
		# User.guessData.repeat.allGuesses.append(guessInput)
		# User.guessData.repeat.guessCount += 1
		# User.guessData.lastGuess.value.value = guessInput