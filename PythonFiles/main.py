# Importing needed modules
import Elem
import Responces
import random
import sys
from time import sleep

# Setting up Print function
def Print (words, speed=0.01):
	for char in words:
		sleep(speed)
		sys.stdout.write(char)
		sys.stdout.flush()

# Setting up random pick function
def pick_random_element():
	global randomElement
	randomElement = random.choice(Elem.Elements)
	if (randomElement.number == 0):
		pick_random_element()

# Setting up Clyde
Bot = Responces.Character("Clyde", "I like computing numbers,\nplaying games,\nrunning new code programs,\nand Watching Mecha Anime.\n(My favorite is Robotics;Notes)")

# Setting up Responces
Respond = Responces.Respond()

# Starting the Talking
Print(Bot.intro)

Print("\n--------------------------------------\n")

Respond.askName()
userName = Respond.userName().userName

# print("")
# print ("Hi " + userName + ", nice to meet you!!!")
# print("And")
# print("WELCOME!!! To my...")
# print("Number Guessing Game of the Elements of the Periodic Table")
# print("---------------------------------------")
# print()
Print('''
Hi ''' + userName + ''', nice to meet you!!
And
WELCOME!!! To my...
Number Guessing Game of the Elements of the Periodic Table 

Here are the rules...
_____________________________________________________
RULES
1. ''' + Bot.name + ''' will pick an element on the Periodic Table.
2. You will have to guess the Atomic Number of that Element (ranging from 1 to 118).
3. ''' + Bot.name + ''' will tell you whether the number is too small or too large.
4. If you guess a number you already guessed, ''' + Bot.name + ''' will notify you on that.  But he will still count that as an attempt.
5. The process repeats until you guess the number.
6. Or until ''' + Bot.name + ''' gets too tired and tells you to stop.
7. As you know, ''' + Bot.name + ''' doesn\'t have all day.
8. Meaning if you can't guess correctly after 60 tries, ''' + Bot.name + ''' will give up on you and reveal the answer.
9. Finally, ''' + Bot.name + ''' will give you your score based on your performances.
10. And you can decided to play again or stop playing the game entirely.
___________________________________________________

Press Enter to Start: ''')

Start = input()

Print('''
Aight, let's start!!!
Give me some time to guess an Element...
[''' + Bot.name + ''' goes brrrr]''')
Print('''
.........................................................................................................................................................................................''', 0.02)