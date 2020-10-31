import random

class Character:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.intro = "Hi, my name is " + self.name + "\n\n" + self.description + "."


class nameAdjs:
	def __init__(self):
		self.first = ["cool", "awesome"]
		self.second = ["splendiferous", "fantastical", "outstanding", "awesome", "fantabulous", "radical"]
		self.chooseFirst = random.choice(self.first)
		self.chooseSecond = random.choice(self.second)

nameAdjs = nameAdjs()

class Respond:
	def askName(self):
		print("Anyways, what " + nameAdjs.chooseFirst + "name do you want me to call you?")
	class userName:
		def __init__(self):
			self.userName = str(input("My " + nameAdjs.chooseSecond + " name is: "))