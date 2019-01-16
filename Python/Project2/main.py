import string
import os
import json
import random
from termcolor import cprint, colored
from board import *

picture1 = r'''
                  Hangman v1.0
                                   
                     ##                                  
                    #° °#                                 
                    # ° #                                 
                    # ▄ #                                 
                     ###                                  
                    #####                                 
                   #######                                
                  ## ### ##                               
                  ## ### ##                               
                     ###                                  
                    #####                                 
                   ### ###                                
                   ###  ###                               
                  ####   ###                                 
'''

picture2 = r'''
                  Hangman v1.0
                              
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
          ▓                         ▓                 
          ▓                         ▓                      
          ▓                         ▓                      
          ▓          ###            ▓                      
          ▓         #° °#           ▓                      
          ▓         #█°█#           ▓                      
          ▓         #███#           ▓                      
          ▓          ###            ▓                      
          ▓         #####           ▓                      
          ▓        #######          ▓                      
          ▓       ## ### ##         ▓                      
          ▓       ## ### ##         ▓                      
          ▓          ###            ▓                      
          ▓         #####           ▓                      
          ▓        ### ###          ▓                      
          ▓        ###  ###         ▓                      
          ▓       ####   ###        ▓                      
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         
'''

picture3 = r'''
                  Hangman v1.0
                              
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
          ▓                         ▓                 
          ▓                         ▓                      
          ▓                         ▓                      
          ▓          ###            ▓                      
          ▓         #° °#           ▓                      
          ▓         #█°█#           ▓                      
          ▓         #███#           ▓                      
          ▓          ###            ▓                      
          ▓         #####           ▓                      
          ▓        #######          ▓                      
          ▓       ## ### ##         ▓                      
          ▓       ## ### ##         ▓                      
          ▓          ###            ▓                      
          ▓         #####           ▓                      
          ▓        ### ###          ▓                      
          ▓        ###  ###         ▓                      
          ▓       ####   ###        ▓                      
          ▓       ▓▀▀▀▀▀▀▀▀▓        ▓                      
          ▓       ▓        ▓        ▓                      
          ▓       ▓        ▓        ▓                      
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         
'''

picture4 = r'''
                  Hangman v1.0
                              
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
          ▓                         ▓                 
          ▓           ▄▄▄▄▄▄▄▄      ▓                      
          ▓                  ▐      ▓                      
          ▓          ###     ▐      ▓                      
          ▓         #° °#    ▐      ▓                      
          ▓         #█°█#    ▐      ▓                      
          ▓         #███#    ▐      ▓                      
          ▓          ###     ▐      ▓                      
          ▓         #####    ▐      ▓                      
          ▓        #######   ▐      ▓                      
          ▓       ## ### ##  ▐      ▓                      
          ▓       ## ### ##  ▐      ▓                      
          ▓          ###     ▐      ▓                      
          ▓         #####    ▐      ▓                      
          ▓        ### ###   ▐      ▓                      
          ▓        ###  ###  ▐      ▓                      
          ▓       ####   ### ▐      ▓                      
          ▓       ▓▀▀▀▀▀▀▀▀▓ ▐      ▓                      
          ▓       ▓        ▓ ▐      ▓                      
          ▓       ▓        ▓ ▐      ▓                      
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         
'''

picture5 = r'''
                  Hangman v1.0
                              
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
          ▓                         ▓                 
          ▓           ▄▄▄▄▄▄▄▄      ▓                      
          ▓           ║      ▐      ▓                      
          ▓          ###     ▐      ▓                      
          ▓         #° °#    ▐      ▓                      
          ▓         #█°█#    ▐      ▓                      
          ▓         #███#    ▐      ▓                      
          ▓          ###     ▐      ▓                      
          ▓         #####    ▐      ▓                      
          ▓        #######   ▐      ▓                      
          ▓       ## ### ##  ▐      ▓                      
          ▓       ## ### ##  ▐      ▓                      
          ▓          ###     ▐      ▓                      
          ▓         #####    ▐      ▓                      
          ▓        ### ###   ▐      ▓                      
          ▓        ###  ###  ▐      ▓                      
          ▓       ####   ### ▐      ▓                      
          ▓       ▓▀▀▀▀▀▀▀▀▓ ▐      ▓                      
          ▓       ▓        ▓ ▐      ▓                      
          ▓       ▓        ▓ ▐      ▓                      
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         
'''

picture6 = r'''
                  Hangman v1.0
                              
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
          ▓                         ▓                 
          ▓           ▄▄▄▄▄▄▄▄      ▓                      
          ▓           ║      ▐      ▓                      
          ▓          ╪║╪     ▐      ▓                      
          ▓         ║° °║    ▐      ▓                      
          ▓         ║█°█║    ▐      ▓                      
          ▓         ║███║    ▐      ▓                      
          ▓         ║╪╪╪╪    ▐      ▓                      
          ▓         #####    ▐      ▓                      
          ▓        #######   ▐      ▓                      
          ▓       ## ### ##  ▐      ▓                      
          ▓       ## ### ##  ▐      ▓                      
          ▓          ###     ▐      ▓                      
          ▓         #####    ▐      ▓                      
          ▓        ### ###   ▐      ▓                      
          ▓        ###  ###  ▐      ▓                      
          ▓       ####   ### ▐      ▓                      
          ▓       ▓▀▀▀▀▀▀▀▀▓ ▐      ▓                      
          ▓       ▓        ▓ ▐      ▓                      
          ▓       ▓        ▓ ▐      ▓                      
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         
'''

picture7 = r'''
                  Hangman v1.0
                              
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
          ▓                         ▓                 
          ▓           ▄▄▄▄▄▄▄▄      ▓                      
          ▓           ║      ▐      ▓                      
          ▓          ╪║╪     ▐      ▓                      
          ▓         ║° °║    ▐      ▓                      
          ▓         ║█°█║    ▐      ▓                      
          ▓         ║███║    ▐      ▓                      
          ▓         ║╪╪╪║    ▐      ▓ 
          ▓         ·  · ·   ▐      ▓                      
          ▓          · ·  ###▐      ▓                      
          ▓          ·#######▐      ▓                      
          ▓         ## ### ##▐      ▓                      
          ▓       ## ### ##  ▐      ▓                      
          ▓         ###  ·   ▐      ▓                      
          ▓      #####    ·  ▐      ▓                      
          ▓    ### ###  ·    ▐      ▓                      
          ▓   ###  ###     · ▐      ▓                      
          ▓  ####   ###      ▐      ▓                                                                
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 

Oouch!        
'''

class HangMan:

	def __init__(self):
		self.wordFile = ""
		self.word = ""
		self.orgWord = ""
		self.translation = ""
		self.ALPHABETS = [letter for letter in string.ascii_uppercase]
		self._tries = 7
		self.entry = []
		self.images = [picture7, picture6, picture5, picture4, picture3, picture2, picture1]
		self.colors = ["red","magenta", "magenta", "cyan","cyan","green", "green"]
		self.currentImage = self.images[-1]
		self.currentColor = self.colors[-1]
		self.getWord()

	
	@property
	def tries(self):
		return self._tries
		
	@tries.setter	
	def tries(self,x):
		self._tries = x
		self.currentImage = self.images.pop()	
		self.currentColor = self.colors.pop()

	def drawImage(self):
		cprint(self.currentImage,self.currentColor)

	def getWord(self):
		with open("dict.json", encoding="utf8") as f:
			data = json.load(f)
			words = list(data.keys())
			self.word = random.choice(words)
			self.translation = "\n".join(data[self.word])
		
	def displayStatus(self):
		os.system("cls")
		status = ""
		print("\n")
		for letter in self.word:
			if letter in self.entry:
				status += letter
			else:
				status += "_"

		cprint("GUESS THE WORD","white","on_blue")
		print()
		cprint(self.translation, "red","on_white")
		print()
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

	game = HangMan()	

	game.displayStatus()

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
					break
			else:
				game.tries -= 1
				game.displayStatus()
				if game.tries == 0:
					game.entry = game.word
					game.displayStatus()
					cprint("YOU LOSE","red" , attrs=['reverse'])
					break
		else:
			game.displayStatus()
			print("{} - invalid input. Choose from available letters\n".format(choice))











