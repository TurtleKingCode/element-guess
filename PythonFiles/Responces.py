import Elem
import random
import sys
from time import sleep

# Setting up Functions and Objects
class Bot:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.intro = "Hi, my name is " + self.name + " 👋 👋 👋\n\n" + self.description + "."
	randomElement = 0
	
	def pickRandomElement(self):
		Bot.randomElement = random.choice(Elem.Elements)
		if Bot.randomElement.number == 0:
			Bot.pickRandomElement(self)

	def Print(self, words, sleep_time=0.01):
		for char in (words + "\n"):
			sleep(sleep_time)
			sys.stdout.write(char)
			sys.stdout.flush()

	def askName(self, user):
		Bot.Print(self, "Anyways, what " + System.generateRandomMessage(System.nameAdjs.first) + " name do you want me to call you?")
		user.name = input("My " + System.generateRandomMessage(System.nameAdjs.second) + " name is: ")


	def Game(self, bot, user):
		reactorResults = user.guessData.guessReactor(bot, user)
		element = bot.randomElement
		if user.guessData.repeat.guessCount >= 60:
			bot.revealResults(bot, user, True)
			exit()
		if int(reactorResults.value) < bot.randomElement.number:
			bot.Print(System.generateRandomMessage(bot.guessResponces(bot, user, element).tooLow))
			if reactorResults.repeated == True:
				bot.Print("Also, you typed that input before. I'm still counting it though. UwU")
			bot.Game(bot, user)
		elif int(reactorResults.value) > bot.randomElement.number:
			bot.Print(System.generateRandomMessage(bot.guessResponces(bot, user, element).tooHigh))
			if reactorResults.repeated == True:
				bot.Print("Also, you typed that input before. I'm still counting it though. UwU")
			bot.Game(bot, user)
		elif int(reactorResults.value) == bot.randomElement.number:
			bot.Print(System.generateRandomMessage(bot.guessResponces(bot, user, element).perfect))
			bot.revealResults(bot, user)
			bot.Print(
'''
			
			
			
-----------------------------------------------------------
Oh, by the way... Do you wanna play again?''')
			playAgain = input("")
			if playAgain == "yes" or playAgain == "Yes" or playAgain == "YES":
				user.guessData.lastGuess.value = 0
				user.guessData.repeat.guessCount = 0
				user.guessData.noRepeat.guessCount = 0
				user.guessData.repeat.allGuesses = []
				user.guessData.noRepeat.allGuesses = []
				bot.Print("Okay...")
				bot.Print("Let's Do it Again")
				bot.Print(
'''Aight, let's start!!!
Give me some time to guess an Element...
[''' + bot.name + ''' goes brrrr]''')
				bot.Print('''........................................''', 0.02)
				bot.pickRandomElement()
				bot.Print('''I Have an Element... Now Start Guessing 😁''')
				bot.Game(bot, user)
			else:
				bot.Print("Okay :)")

	class guessResponces:
		def __init__ (self, bot, user, element):
			self.tooLow = ["Too Small", "Not High Enough", "Not Heavy Enough", user.guessData.lastGuess.element().name + " Doesn't Have Enough Protons", "Your Atomic Number Needs to Get Bigger", "My Element is Heavier", bot.name + " Wants More More MORE!!!!", "Directions: 👆"]
			self.tooHigh = ["Too Big", "Not Low Enough", "That's More Than Enough, Go Down Pal", user.guessData.lastGuess.element().name + " Has Too Many Protons", "Your Atomic Number Needs to Get Smaller", "My Element is Lighter", bot.name + " Says You're Too Far Ahed", "Direction: 👇"]
			self.perfect = ["Perfect!!!", "You Got It", bot.name + " is Proud of You", "You Got is Right, " + element.name + " Was the Element I Had In Mind", "That's Just the Right # of Protons", bot.name + " Is Very Proud of You. For Guessing the Number", "You Just Made " + bot.name + " Proud.  UwU", "👍 👍 👍"]
	def revealResults(self, bot, user, forced = False):
		attempts = User.guessData.repeat.guessCount
		noRepeatAttempts = User.guessData.noRepeat.guessCount
		attemptsList = User.guessData.repeat.allGuesses
		noRepeatList = User.guessData.noRepeat.allGuesses
		guessScore = 0
		if attempts <= 7:
			guessScore = ((7 - attempts + 1) * (7 - attempts + 2)) / 2 + 52
		else:
			guessScore = 59 - attempts
		if forced == True:
			bot.Print("\n\nI'm Sorry to have Stopped you short, I get tired after 59 tries, and you really reached that")
		bot.Print(
'''------------------------------------------------------------------------------
The Element of the Periodic Table I picked was '''+ bot.randomElement.name + '''
With the Symbol of ''' + bot.randomElement.symbol + '''
And an Atomic Number of ''' + str(bot.randomElement.number) + '''.
NoW ''')
		bot.Print(
'''
Here are your stats:
Total Attempts: ''' + str(attempts) + '''
List of Attempts: ''' + str(attemptsList) + '''
Now, because Franklin Wants all those Points for the Coding Challenge...
Total Attempts (minus the repeated ones): ''' + str(noRepeatAttempts) + '''
List of Attempts (minus the repeated ones): ''' + str(noRepeatList) + '''
Finally, As for you calculated score...

YOU GOT ''' + str(int(guessScore)) + ''' Points!!!

Thanks alot ''' + user.name + ''' for Playing With Me...
You Made ''' + bot.name + ''' Very Happy ☺️
I Hope to Possibly See You Some Time Later.
(And hopefully not in a Python Project)
According to Franklin, Making this in Node.js Would Have Been Easier On Him...
"Objects are So Complicated In Python" -- He Says.

Anyways...
''' + bot.name + ''' Says BYEEE 👋 👋 👋''')


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
	guessInput = 0
	name = ""
	class guessData:
		class lastGuess:
			value = 0
			def element():
				reNewedElement = Elem.Elements[int(User.guessData.lastGuess.value)]
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
					else:
						User.guessData.lastGuess.value = int(guess)
						User.guessData.repeat.guessCount += 1
						User.guessData.repeat.allGuesses.append(User.guessData.lastGuess.value)
						User.guessData.noRepeat.guessCount += 1
						User.guessData.noRepeat.allGuesses.append(User.guessData.lastGuess.value)
			return User.guessData.results(guess, Num, intBool, User.guessData.guessReactor)