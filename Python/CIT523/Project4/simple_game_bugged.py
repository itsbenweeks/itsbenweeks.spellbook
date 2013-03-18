# Simple buggy Game
# I started by replacing all inputs with raw_input
import random
class Player(object):
    """ A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
	
	return response

def ask_number(low, high, question):
	"""Ask for a number within a range."""
	response = None
	while response not in range(low, high+1):
		response = int(raw_input(question))
	return response
#Typo for variable question, changed from questio=>question, corrected for loop, added a return statement

print("Welcome to the world's simplest game!\n")
#The again variable was being called before being instantiated.
again = ''
while again != "n":
    players = []
    num = ask_number(2, 5,"How many players? (2 - 5): ")
    for i in range(num):
        name = raw_input("Player name: ")
        score = random.randint(1,100)
		#modified random.range to randint functioninstead.
        player = Player(name, score)
        players.append(player)

    print("\nHere are the game results:")
    for player in players:
        print(player)
    
    again = ask_yes_no("\nDo you want to play again? (y/n): ")

input("\n\nPress the enter key to exit.")
