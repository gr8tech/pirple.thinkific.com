'''
Python Homework Assignment 6
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

Advanced Loops: Drawing a drawing board
'''
import os

def drawBoard(rows, columns):
	'''
	Draws a board given rows and columns dimensions of the board
	Args:
		rows - integer representing the height of the board
		columns - integer representing the width of the board
	Returns:
		True - board was succesfuly drawn
		False - board dimensions exceeded terminal dimensions
	'''
	terminalSize = os.get_terminal_size() #obtain the dimensions of the terminal window
	if columns <= terminalSize.columns and rows <= terminalSize.lines:
	    for row in range(rows):
	        if row % 2 == 0:
	            for column in range(columns):
	                if column % 2 == 0:
	                    print(" ", end="")
	                else:
	                    print("|", end="")
	            print() # print newline after completion of row printing
	        else:
	        	print("-" * columns)
	    return True
	else:
		return False        	

print(drawBoard(5,5))
