'''
Python Project #1
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com
OS: Windows 10
Python: 3.
Require Modules: termcolor, colorama

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
import os
import colorama	
from termcolor import cprint

ROWS = 6 # number of rows of board
COLUMNS = 7 # number of columns of board
HEADERS = ["A","B","C","D","E","F","G"] # column identifiers
# color for display messages
WARNING_COLOR = "red"
# symbols to distinguish player pieces
PLAYER_SYMBOLS = {
	1: "X",
	2: "O"
}
# colors to distinguish player pieces and communication
PLAYER_COLORS = {
	1:"green",
	2:"blue"
}
'''
COORDINATES FOR DIAGONAL CHECKS
(a,b),(a`,b`)
a - row start position
b - column start position
a` - row end position
b` - column end position
'''
# Coordinates for checking diagonal SW to NE combinations for win
DIAGONAL_SW_NE = [((3,0),(0,3)),((4,0),(0,4)),((5,0),(0,5)),
					((5,1),(0,6)),((5,2),(1,6)),((5,3),(2,6))]
# Coordinates for checking diagonal NW to SE combinations for win
DIAGONAL_NW_SE = [((2,0),(5,3)),((1,0),(5,4)),((0,0),(5,5)), 
					((0,1),(5,6)), ((0,2),(4,6)),((0,3),(3,6))]
'''
Structure for how the coordinates are used
SW-NE Direction:
	row index Decreases by an offset of 1 and a step of 1
NW-SE Direction:
	row index Increases by an offset of 1 and a step of 1	
'''
DIAGONALS = [
	{
		"offset":-1,
		"step":-1,
		"coordinates":DIAGONAL_SW_NE 
	},
	{
		"offset":1,
		"step":1,
		"coordinates":DIAGONAL_NW_SE 
	}	
]

# Board data and player moves stored in here
boardData = []
# Identifies the next free slot in a column
positionPointer = []
# holder for current player
player = 1	

def CheckDraw():
	'''
	Checks if the game has drawn
	All input fields are field up and there is no winner
	Returns:
		True - Game has drawn
		False - Game has not been drawn
	'''
	for column in  boardData:
		colData = "".join(column).replace(" ","")
		if len(colData) < ROWS:
			return False
	return True

def CheckDiagonals(direction = "NW-SE"):
	for diagonal in DIAGONALS:
		for group in diagonal["coordinates"]:
			startPosition = group[0]
			endPosition = group[1]
			diagData = ""
			col = startPosition[1]
			offset = diagonal["offset"]
			step = diagonal["step"]
			for row in range(startPosition[0],endPosition[0]+ offset,step):
				diagData += boardData[col][row]
				col += 1
			for value in PLAYER_SYMBOLS.values():
				if value * 4 in diagData:
					return True
	return False

def CheckHorizontal():
	'''
	Checks for 4 connected symbols on the horizontal plane
	Since boardData is stored in columns, the column array is
	1st transposed	
	'''
	transposedBoardData = list(zip(*boardData))
	for row in transposedBoardData:
		rowData = "".join(row)
		for value in PLAYER_SYMBOLS.values():
			if value * 4 in rowData:
				return True
	return False

def CheckVertical():
	'''
	Check column array in boardData for 4 connected symbols
	from either player 1 or player 2
	Returns:
		True - Connected 4 symbols found
		False - Connected 4 symbols not found
	'''
	for column in boardData:
		colData = "".join(column)
		for value in PLAYER_SYMBOLS.values():
			if value * 4 in colData:
				return True
	return False
				
def GameWon():
	'''
	Checks if the game has been won by the current player
	Returns:
		True - Game won
		False - Game has not been won
	'''
	if CheckHorizontal(): # Check Horizontal direction
		return True
	elif CheckVertical(): # Check Vertical direction
		return True
	elif CheckDiagonals(): # Check Diagonal directions
		return True
	else:
		return False

def GetSymbolColor(symbol):
	'''
	Retrives the color to be applied to a given symbol
	Args:
		symbol - Player Symbol
	Returns:
		color - players color
	'''
	for key in PLAYER_SYMBOLS:
		if PLAYER_SYMBOLS[key] == symbol:
			return PLAYER_COLORS[key]
	return "white" 

def updateBoardData(column):
	'''
	Updates the Board data
	Args:
		column -  column selected by current player
	Returns:
		True - boardData successfully updated
		False - The selected column if full
	'''
	columnIndex = HEADERS.index(column)
	nextPosition = positionPointer[columnIndex]
	if nextPosition >= 0:
		boardData[columnIndex][nextPosition] = PLAYER_SYMBOLS[player]
		positionPointer[columnIndex] -= 1
		return True
	else:
		return False 

def initPositionPointer():
	'''
	Initializes the position pointers to point to the bottom
	of all columns
	'''
	for _ in range(COLUMNS):
		positionPointer.append(ROWS-1)

def initBoardData():
	'''
	Initializes the boardData with empty (" ") values
	'''
	for i in range(COLUMNS):
		tempArray = []
		for j in range(ROWS):
			tempArray.append(" ")
		boardData.append(tempArray)

def drawBoard():
	'''
	Draw/Refresh the Game Board
	'''
	# Clear the console
	os.system("cls")
	# Display some information
	cprint("Connect 4 v1.0","green")
	totalVerticalLines = (COLUMNS * 2) + 1
	print("=" * totalVerticalLines)
	headerIndex = 0
	for i in range(ROWS + 1):
		for j in range(totalVerticalLines):
			if j % 2 == 0:
				print("|",end="")
			else:
				if i == 0:
					# printer column HEADERS
					cprint(HEADERS[headerIndex],
				"green", end="")
					headerIndex += 1
				else:
					col = j // 2
					row = i-1
					symbol = boardData[col][row]
					color = GetSymbolColor(symbol)
					cprint(boardData[col][row],
						color,end="")
		print()
		print("-" * totalVerticalLines)
	# display some information
	cprint("KEY","green")
	cprint("Player 1 - {}".format(PLAYER_SYMBOLS[1]),
		PLAYER_COLORS[1])
	cprint("Player 2 - {}".format(PLAYER_SYMBOLS[2]),
		PLAYER_COLORS[2])
	cprint("Enter Q to Quit the game","red")
	print()

# for initializing the color scheme on my console.
colorama.init()
# initialize board data
initBoardData()
# initialize position pointers
initPositionPointer()
# draw the board for 1st run
drawBoard()

# Enter the game loop
while True:
	'''
	get input from player. Players are requested for input in their
	own color
	'''
	cprint("Player {} : Select Column >> ".format(player),
		PLAYER_COLORS[player],end="")
	choice = input().strip().upper()

	if choice in HEADERS:
		if updateBoardData(choice):
			drawBoard()
			if GameWon():
				cprint("Player {} has won the game". format(player),
					"red")
				break;
			if CheckDraw():
				cprint("The game has drawn","red")
			if player == 1:
				player = 2
			else:
				player = 1
		else:
			drawBoard()
			cprint("Error: Column {} is full".format(choice),
			WARNING_COLOR)	
	elif choice == "Q":
		cprint("Player {} has quit the game".format(player),"red")
		break
	else:
		cprint("Error: Column {} does not exist".format(choice),
			WARNING_COLOR)