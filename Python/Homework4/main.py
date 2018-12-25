'''
Python Homework Assignment 4
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

Lists
'''

myUniqueList = []
myLeftovers = []

def addToList(value):
	'''
	Adds provided value to myUniqueList if it does not exist.
	Args:
		value - value to be added to the list
	Returns:
		True - if value is not present in the list. Accepted value is saved in myUniqueList list
		False - if the value already exists in the list. Reject value is saved in myLeftovers list
	'''
	if value in myUniqueList:
		# save value to myLeftovers if already in myUniqueList
		saveLeftovers(value)
		return False
	else:
		myUniqueList.append(value)
		return True

def saveLeftovers(value):
	'''
	Adds rejected values to myLeftovers list
	'''
	myLeftovers.append(value)


# Function tests
# Returns True
print(addToList(1))
# Returns True
print(addToList(2))
# Returns True
print(addToList(3))
# Returns False
print(addToList(1))
print("Accepted Values")
print(myUniqueList)
print("Rejected values")
print(myLeftovers)
