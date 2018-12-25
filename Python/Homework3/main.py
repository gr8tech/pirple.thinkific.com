'''
Python Homework Assignment 3
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

`If` statements; Comparison of numbers
'''

def number_match(num1, num2, num3):
	'''
	Functions checks if 2 or more of the given numbers are equal
	Args:
		num1, num2, num3
		num1, num2, num3 can be an Integer or an Integer string
	Returns:
		True if 2 or more numbers are equal, False otherwise
	Examples:
		number_match(1,2,1) returns True
		number_match(1,2,"1") returns True
		number_match(1,2,3) return False
	Logic:
		There are three posibilities
		1. num1 is equal to num2 OR
		2. num1 is equal to num3 OR
		3. num2 is equal to num3
	'''
	num1, num2, num3 = int(num1), int(num2), int(num3)
	if (num1 == num2) or (num1 == num3) or (num2 == num3):
		return True
	else:
		return False

# Function tests
# Returns False
print(number_match(1,2,3))
# Returns True
print(number_match(1,2,1))
#Returns True
print(number_match("5",6,5)) 
