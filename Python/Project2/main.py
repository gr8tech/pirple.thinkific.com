'''
Python Project #2
Course: Python is Easy @ pirple
Program: Hangman
Author: Moosa
Email: gr8tech01@gmail.com
OS: Windows 10
Python: 3.x
Require Modules: termcolor

Starting the game

python main.py [--hints] [--single]

--hints:
	optional, to display game hints
--single:
	optional, to play a single game

'''

import argparse
import string
import os
import json
import random
from termcolor import cprint, colored
from board import *
from image import *


class HangMan:
	'''
	Represents the Hangman class
	'''

	def __init__(self, showHints=False, singleGame=False, gamesPlayed=0, gamesWon=0):
		# cumulative number of games played in a continous game
		self.gamesPlayed = gamesPlayed
		# cumulative number of games played in a contionous game
		self.gamesWon = gamesWon
		# display word translation and wrong attempts left
		self.showHints = showHints
		# indentifies if game is single or contionous
		self.singleGame = singleGame
		# the word to be guessed as represented on the game display
		self.word = ""
		# the word to be guessed
		self.orgWord = ""
		# translation of the word to be guessed
		self.translation = ""
		# letters of the alphabet, capitalized
		self.ALPHABETS = list(string.ascii_uppercase)
		# tracks accepted letters entred by player
		self.entry = []
		# list of images to be displayed during game play and their respective colors
		self.gameImages = list(zip([picture6, picture5, picture4, picture3, picture2, picture1, picture1],
					["red","magenta", "magenta", "cyan","cyan","green", "green"]))
		# number of allowed wrong attempts
		self._tries = len(self.gameImages)
		# 1st image to be displayed
		self.currentImage = self.gameImages[-1]
		# retrive the game word
		self.getWord()
		# clear the screen
		os.system('cls')
		# display the initial game display
		self.displayStatus()

	
	@property
	def tries(self):
		'''
		Returns number of wrong attempts left
		'''
		return self._tries
		
	@tries.setter
	def tries(self,x):
		# update wrong attempts left
		self._tries = x
		self.currentImage = self.gameImages.pop()

	def drawImage(self):
		'''
		Display the current image
		'''
		cprint(self.currentImage[0],self.currentImage[1])

	def getWord(self):
		'''
		Gets a random word from the dict.json file for the game
		This is a large dictionary of English words and their translations
		'''
		# open the dict.json file
		with open("dict.json", encoding="utf8") as f:
			# convert json into a Python object
			data = json.load(f)
			# extract list of all words  
			words = list(data.keys())
			# select a random word
			self.word = random.choice(words)
			# get the translation of the word
			self.translation = data[self.word]
		
	def displayHints(self):
		'''
		Displays hints with regards to the word to be guessed.
		Provides:
			Translation of the word
			Games Played, in a continous game
			Games Won, in a continous game
			Wrong attempts left
		'''
		cprint("HINTS", "white", "on_blue")
		cprint(" ; ".join(self.translation), "white","on_magenta")
				
		print()
		cprint("{} Wrong attemps left".format(self.tries),"red")
		cprint("{} Games Played".format(self.gamesPlayed),"red")
		cprint("{} Games Won".format(self.gamesWon),"red")
		print()

	def displayStatus(self):
		'''
		Display the current status of the game
		Returns:
			True - game has been won
			False - otherwise
		'''
		# clear the screen
		os.system("cls")
		# draw the Hangman image
		self.drawImage()
		status = ""
		# configure current state of guessed word
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

	def removeAcceptedChoice(self, choice):
		'''
		Removes accepted letter from the list of possible letters
		'''
		for idx, letter in enumerate(self.ALPHABETS):
			if letter == choice:
				self.ALPHABETS[idx] = " "
				break	


if __name__ == "__main__":
	
	# set up the command line arguments
	parser = argparse.ArgumentParser()
	# optional argument, to show hints, default is False
	parser.add_argument(
		'--hints', dest='showHints',  action='store_true',  default=False, help='display hints')
	# optional argument to play a single/continous game, default is continous game
	parser.add_argument(
		'--single', dest='singleGame',  action='store_true',  default=False, help='play single game')
	args = parser.parse_args()

	# initialize the game
	game = HangMan(args.showHints, args.singleGame)	

	#game loop
	while True:
		# get user choice
		choice = input("Enter a letter: ").strip().upper()
		# validate choice
		if choice == "EXIT":
			# exit game if exit inputted by user
			# display the word to be guessed
			game.entry = game.word
			game.displayStatus()
			break
		elif choice in game.entry:
			# if selected letter is available, display an error message
			game.displayStatus() # update game display board
			print("{} - has been used\n".format(choice))
		elif choice in game.ALPHABETS:
			if choice in game.word:
				# if chosen letter is in word to be guessed, add it to the entry list
				game.entry.append(choice)
				# remobe the accepted letter from list of possible choice of letters
				game.removeAcceptedChoice(choice)
				if game.displayStatus(): # update game board
					game.gamesWon += 1 
					game.gamesPlayed += 1
					cprint("YOU WIN","green",attrs=['reverse'])
					if game.singleGame:
						break
					else:
						input("Press Enter to continue...")
						# reset game for a continous game, when game has been completed with either WIN/LOSS
						game = HangMan(game.showHints, game.singleGame, game.gamesPlayed, game.gamesWon)
			else:
				# reduce attemps left if chosen letters is not present in the word
				game.tries -= 1
				game.displayStatus() # update the display
				if game.tries == 0:
					# Game has been lost if tries/attemps = 0
					game.gamesPlayed += 1
					game.entry = game.word
					game.displayStatus()
					cprint("YOU LOSE","red" , attrs=['reverse'])
					if game.singleGame:
						break
					else:
						input("Press Enter to continue...")
						# reset game for a continous game, when game has been completed with either WIN/LOSS
						game = HangMan(game.showHints, game.singleGame, game.gamesPlayed, game.gamesWon)
		else:
			game.displayStatus()
			print("{} - invalid input. Choose from available letters\n".format(choice))
