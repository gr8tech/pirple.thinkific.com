import argparse
import string
import os
import json
import random
from termcolor import cprint, colored
from board import *
from image import *


class HangMan:

	def __init__(self, showHints, singleGame):
		self.showHints = showHints
		self.singleGame = singleGame
		self.wordFile = ""
		self.word = ""
		self.orgWord = ""
		self.translation = ""
		self.ALPHABETS = [letter for letter in string.ascii_uppercase]
		self.entry = []

		self.gameImages = list(zip([picture6, picture5, picture4, picture3, picture2, picture1, picture1],
					["red","magenta", "magenta", "cyan","cyan","green", "green"]))
		self._tries = len(self.gameImages)
		self.currentImage = self.gameImages[-1]
		
		self.getWord()
		os.system('cls')


		self.displayStatus()

	
	@property
	def tries(self):
		return self._tries
		
	@tries.setter	
	def tries(self,x):
		self._tries = x
		self.currentImage = self.gameImages.pop()

	def drawImage(self):
		cprint(self.currentImage[0],self.currentImage[1])

	def getWord(self):
		with open("dict.json", encoding="utf8") as f:
			data = json.load(f)
			words = list(data.keys())
			self.word = random.choice(words)
			self.translation = data[self.word]
		
	def displayHints(self):
		i = 0
		cprint("HINTS", "white", "on_blue")
		for idx, translation in enumerate(self.translation):
			if i == 0:
				cprint(str(idx + 1) + " : " + translation, "white","on_magenta")
				i = 1
			elif i == 1:
				cprint(str(idx + 1) + " : " + translation, "white","on_cyan")
				i = 0
		print()
		cprint("{} Wrong attemps left".format(self.tries),"red")
		print()

	def displayStatus(self):
		os.system("cls")
		self.drawImage()
		status = ""
		for letter in self.word:
			if letter in self.entry:
				status += letter
			else:
				status += "_"

		cprint("GUESS THE WORD","white","on_blue")
		print()
		if self.showHints:
			self.displayHints()
		drawDisplay(status)
		drawKeyPad(self.ALPHABETS)
		

		if status == self.word:
			return True
		else:
			return False

	def displayOptions(self):
		print(" ".join(self.ALPHABETS))
		print()
		print("{} Attempts left\n".format(self.tries))
		print("Enter EXIT to Quit the Game\n")

	def removeAcceptedChoice(self, choice):
		for idx, letter in enumerate(self.ALPHABETS):
			if letter == choice:
				self.ALPHABETS[idx] = " "
				break	


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--hints', dest='showHints',  action='store_true',  default=False, help='display hints')
	parser.add_argument(
		'--single', dest='singleGame',  action='store_true',  default=False, help='play single game')
	args = parser.parse_args()

	game = HangMan(args.showHints, args.singleGame)	

	#game loop
	while True:
		choice = input("Enter a letter: ").strip().upper()
		# validate choice
		if choice == "EXIT":
			game.entry = game.word
			game.displayStatus()
			break
		elif choice in game.entry:
			game.displayStatus()
			print("{} - has been used\n".format(choice))
		elif choice in game.ALPHABETS:
			if choice in game.word:
				game.entry.append(choice)
				game.removeAcceptedChoice(choice)
				if game.displayStatus():
					cprint("YOU WIN","green",attrs=['reverse'])
					if game.singleGame:
						break
					else:
						input("Press Enter to continue...")
						game = HangMan(game.showHints, game.singleGame)
			else:
				game.tries -= 1
				game.displayStatus()
				if game.tries == 0:
					game.entry = game.word
					game.displayStatus()
					cprint("YOU LOSE","red" , attrs=['reverse'])
					if game.singleGame:
						break
					else:
						input("Press Enter to continue...")
						game = HangMan(game.showHints, game.singleGame)
		else:
			game.displayStatus()
			print("{} - invalid input. Choose from available letters\n".format(choice))
