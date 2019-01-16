import string
from termcolor import cprint, colored

'''
╔═══════════════════════╗
║                       ║
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
def centerWord(word):
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
	word = centerWord(word)
	print("╔═════════════════════════════════════╗")
	print("║ {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} ║".format(*word))
	print("╚═════════════════════════════════════╝")

def drawKeyPad(alphabet=string.ascii_uppercase):
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

drawDisplay("HELLO WORLD")
drawKeyPad()
