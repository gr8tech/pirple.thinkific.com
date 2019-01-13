import string
import os
import json
import random


class HangMan:

	def __init__(self):
		self.wordFile = ""
		self.word = ""
		self.ALPHABETS = [letter for letter in string.ascii_uppercase]
		self.tries = 7
		self.entry = []		
		self.setLevel()
		self.getWord()

	def setLevel(self):
		while True:
			os.system("cls")
			print("Select your Level")
			print("1. Easy")
			print("2. Hard")
			choice = input("1/2: ")
			if choice == "1":
				self.wordFile = "easy.txt"
				break
			elif choice == "2":
				self.wordFile = "hard.txt"
				break		

	def getWord(self):
		with open(self.wordFile) as f:
			self.word = random.choice(f.readlines()).strip().upper()

	def displayStatus(self):
		os.system("cls")
		status = ""
		print("\n")
		for letter in self.word:
			if letter in self.entry:
				status += letter
				print(letter,end=" ")
			else:
				print("_", end=" ")
		print("\n")
		if status == self.word:
			return True
		else:
			return False

	def displayOptions(self):
		print(" ".join(self.ALPHABETS))
		print()
		print("{} Wrong attempts left\n".format(self.tries))
		print("Enter EXIT to Quit the Game\n")


if __name__ == "__main__":

	game = HangMan()	

	game.displayStatus()
	game.displayOptions()

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
			game.displayOptions()
			print("{} - has been used\n".format(choice))
		elif choice in game.ALPHABETS:
			if choice in game.word:
				game.entry.append(choice)
				game.ALPHABETS.remove(choice)
				if game.displayStatus():
					print("YOU WIN")
					break
				game.displayOptions()
			else:
				self.tries -= 1
				game.displayStatus()
				game.displayOptions()
				if tries == 0:
					game.entry = game.word
					game.displayStatus()
					print("YOU LOSE")
					break
		else:
			game.displayStatus()
			game.displayOptions()	
			print("{} - invalid input. Choose from available letters\n".format(choice))











