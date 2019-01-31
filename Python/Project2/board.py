'''
GAME DISPLAY WITH KEYPAD TO SHOW AVAILABLE OPTIONS
╔═══════════════════════╗
║        W O R D        ║
╚═══════════════════════╝
┌───┬───┬───┬───┬───┬───┐
│ A │ B │ C │ D │ E │ F │
├───┼───┼───┼───┼───┼───┤
│ G │ H │ I │ J │ K │ L │
├───┼───┼───┼───┼───┼───┤
│ M │ N │ O │ P │ Q │ R │
├───┼───┼───┼───┼───┼───┤
│ S │ T │ U │ V │ W │ X │
│───┼───┼───┼───┼───┼───┤
│   │   │ Y │ Z │   │   │
└───┴───┴───┴───┴───┴───┘
'''

import string
from termcolor import cprint, colored


def centerWord(word):
	'''
	Adds blanks to centre the word shown in the Game Display
	Args:
		word - word to be displayed
	Returns:
		word with fillers before and after
	'''
	displayLen = 18
	left = 0
	right = 0
	placeHolderLen = displayLen - len(word)
	if placeHolderLen % 2 == 0:
		left = right = (displayLen-len(word))//2
	else:
		left = (displayLen - len(word) + 1) // 2
		right = (displayLen - len(word)) // 2
	return [" "] * left + [letter for letter in word] + [" "] * right

def drawDisplay(word):
	'''
	Draws the game display and inserts the WORD
	Args:
		word - word to be displayed
	'''
	word = centerWord(word)
	print("╔═════════════════════════════════════╗")
	print("║ {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} ║".format(*word))
	print("╚═════════════════════════════════════╝")

def drawKeyPad(alphabet=string.ascii_uppercase):
	'''
	Draws the keypad showing available options
	Args:
		alphabet - letters available for selection
	'''
	alphabet = [letter for letter in alphabet]
	print()
	print("CHOOSE FORM THE FOLLOWING LETTERS")
	print("       ┌───┬───┬───┬───┬───┬───┐")
	
	groups = 5
	for i in range(0,len(alphabet),6):
		letters = alphabet[i:6+i]
		if i < 24:
			print("       │ {} │ {} │ {} │ {} │ {} │ {} │".format(*letters))
			print("       ├───┼───┼───┼───┼───┼───┤")
		else:
			print("       │   │   │ {} │ {} │   │   │".format(*letters))
			print("       └───┴───┴───┴───┴───┴───┘")
	print()

# testing
if __name__ == "__main__":
	drawDisplay("HELLO WORLD")
	drawKeyPad()