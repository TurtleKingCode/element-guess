# Importing needed modules
import Elem
import Responces
import random

# Setting up Clyde
Clyde = Responces.Character("Clyde", "I like computing numbers,\nplaying games,\nrunning new code programs,\nand Watching Mecha Anime.\n(My favorite is Robotics;Notes)")

# Setting up Responces
Respond = Responces.Respond()

# Starting the Talking
print(Clyde.intro)

print("\n--------------------------------------\n")

Respond.askName()
userName = Respond.userName().userName

# print("")
# print ("Hi " + userName + ", nice to meet you!!!")
# print("And")
# print("WELCOME!!! To my...")
# print("Number Guessing Game of the Elements of the Periodic Table")
# print("---------------------------------------")
print('''
Hi ''' + userName + ''', nice to meet you!!
And
WELCOME!!! To my...
Number Guessing Game of the Elements of the Periodic Table 
---------------------------------------
''')
# print("")
# print(Respond.userName().username)

# print(type(Respond.userName()))
# print(Respond.userName() + "Yes")

# print(Elem.Elements[0].name)
# print (Responces.Intro)