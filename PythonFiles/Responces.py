class Character:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.intro = "Hi, my name is " + self.name + ", " + self.description + "."
