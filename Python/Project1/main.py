'''
Python Project #1
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

Connect 4 Textual Game
|A|B|C|D|E|F|G|
---------------
|X|X|O|O|X|O|X|
---------------
|O|X|O|X|O|X|O|
---------------
|O|O|X|X|X|O|X|
---------------
|X|O|X|O|X|O|X|
---------------
|X|O|X|O|X|O|X|
---------------
|X|X|O|O|O|X|O|
---------------
'''
import colorama	
from termcolor import cprint

ROWS = 6
COLUMNS = 7
HEADERS = "ABCDEFG"

boardData = []
positionPointer = []

def initPositionPointer():
	for _ in range(COLUMNS):
		positionPointer.append(ROWS-1)

def initBoardData():
	for i in range(ROWS):
		tempArray = []
		for j in range(COLUMNS):
			tempArray.append(" ")
		boardData.append(tempArray)

def drawBoard():
	totalVerticalLines = (COLUMNS * 2) + 1
	headerIndex = 0
	for i in range(ROWS + 1):
		for j in range(totalVerticalLines):
			if j % 2 == 0:
				print("|",end="")
			else:
				if i == 0:
					cprint(HEADERS[headerIndex],
				"green", end="")
					headerIndex += 1
				else:
					print(" ",end="")
		print()
		print("-" * totalVerticalLines)
	cprint("KEY","green")
	cprint("Player 1 - X","red")
	cprint("Player 2 - O","blue")
	print()

colorama.init()
initBoardData()
initPositionPointer()
drawBoard()
print(boardData)
print(positionPointer)

while True:
	Player = 1
	cprint("Player {} : Select Column (A-G) >> ".format(Player),
		"red",end="")
	choice = input().lower()
	break


print(boardData)
print(positionPointer)
