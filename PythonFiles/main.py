# Importing needed modules
# import Elem
import Responces
# import random

# Setting up Clyde
Clyde = Responces.Bot("Clyde", "I like computing numbers, 💻\nplaying games, 🎮\nrunning new code programs,\nand Watching Mecha Anime. 📺\n(My favorite is Robotics;Notes)")

# Setting up Responces
User = Responces.User()

# Starting the Talking
Clyde.Print(Clyde.intro)

Clyde.Print("\n--------------------------------------\n")

Clyde.askName(User)

Clyde.Print('''
Hi ''' + User.name + ''', nice to meet you!!
And
WELCOME!!! To my...
Number Guessing Game of the Elements of the Periodic Table 

Here are the rules...''')
Clyde.Print('''
_____________________________________________________
RULES
1. ''' + Clyde.name + ''' will pick an element on the Periodic Table.
2. You will have to guess the Atomic Number of that Element (ranging from 1 to 118).
3. ''' + Clyde.name + ''' will tell you whether the number is too small or too large.
4. If you guess a number you already guessed, ''' + Clyde.name + ''' will notify you on that.  But he will still count that as an attempt.
5. The process repeats until you guess the number.
6. Or until ''' + Clyde.name + ''' gets too tired and tells you to stop.
7. As you know, ''' + Clyde.name + ''' doesn\'t have all day.
8. Meaning if you can't guess correctly after 59 tries, ''' + Clyde.name + ''' will give up on you and reveal the answer.
9. Finally, ''' + Clyde.name + ''' will give you your score based on your performances.
10. And you can decided to play again or stop playing the game entirely.
___________________________________________________''', 0.005)

Clyde.Print('''Press Enter to Start: ''')

Start = input()

Clyde.Print('''
Aight, let's start!!!
Give me some time to guess an Element...
[''' + Clyde.name + ''' goes brrrr]''')
Clyde.Print('''........................................''', 0.02)

# Actually starting the game itself
Clyde.Print('''I Have an Element...
Now Start Guessing 😁''')

Clyde.pickRandomElement()
Clyde.Game(Clyde, User)