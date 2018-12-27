'''
Python Homework Assignment 8
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

Input and Output
'''

import os

def replaceLine(filename, lineNumber, data):
	'''
	Replaces a given line in the file, with user provided data
	Args:
		filename - file location
		lineNumber - index of line to replace. Indexing starts at 0
		data - user provided data 
	'''
	lines = []
	with open(filename) as file:
		# read all lines from file into an array
		lines = file.readlines()
		# insert a newline if replaced line is not the last line
		if lineNumber != len(lines) - 1:
			lines[lineNumber] = data + "\n"
		else:
			lines[lineNumber] = data

	# save lines to file
	with open(filename,"w") as file:
		file.writelines(lines)	

def saveData(filename, data, mode):
	'''
	Saves user provided data into a file
	Args:
		filename - file location to save the contents
		data - user provided data to save to file
		mode - file access mode w/a
	'''
	with open(filename,mode) as file:

		if mode == "w":
			file.write(data)
		elif mode == "a":
			# if file is empty, do not put a new line
			if os.path.getsize(filename) == 0:
				file.write(data)
			else:
				file.write("\n" + data)
		else:
			print("Error, unknown file mode provided")
		
def displayMessage():
	'''
	Displays user options if the provided file already exists
	Returns:
		User choice A/B/C/D
	'''
	print(r"""
THE PROVIDED FILE ALREADY EXISTS.
Select one of the following options
A) Read the file
B) Delete the file and start over
C) Append the file
D) Replace a single line
		""")
	return input("Select option A/B/C/D: ").strip().upper()

def displayFileContents(filename, showNumbers=False):
	'''
	Displays the contents of the file
	Args:
		filename - location of file to be read
		showNumbers - optional, display the respective line number starting from 1.
	Returns:
		Number of lines in the file
	'''
	linesInFile = 0
	with open(filename) as file:
			for line in file:
				linesInFile += 1
				if showNumbers:
					print(str(linesInFile)+".",line,end="")
				else:
					print(line,end="")
	return linesInFile


def startOver(filename):
	'''
	Delete the old file and create a new empty file
	Args:
		filename - file to be deleted
	'''
	os.remove(filename)
	with open(filename,"w"):
		pass

#  Get the filename
filename = input("Please provide a file location: ")

# Check if the file exists
if os.path.exists(filename) and os.path.isfile(filename):

	#  display and get user choice
	option = displayMessage()

	# read the file
	if option == "A":
		displayFileContents(filename)
	# delete the file and save new data
	elif option == "B": 
		startOver(filename)
	# append data to the file
	elif option == "C":
		data = input("Enter your data: ")
		saveData(filename, data,"a")
	# replace a line in the file
	elif option == "D":
		# display lines in the file
		lineCount = displayFileContents(filename, True)
		print()
		# get line number to be replaced
		lineNumber = int(input("Enter the line number to replace: "))
		# validate line number provided by user
		if lineNumber <= lineCount and lineNumber >= 1:
			data = input("Enter your data: ")
			# user line numbers start from 1, whilst the program uses line numbers from 0
			# internally to access file contents
			replaceLine(filename, lineNumber-1, data)
		else:
			print("Invalid line number provided")
	else:
		print("The provided option is unknown")

else:
	# if file does not exist, create a new one and save data
	data = input("Enter your data: ")
	saveData(filename, data,"w")