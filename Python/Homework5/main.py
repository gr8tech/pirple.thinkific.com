'''
Python Homework Assignment 5
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

FizzBuzz Problem, with an additional check for prime numbers
'''

def FizzBuzzPrime():
	'''
	Generates numbers from 1 to 100
	Output:
		Prints "Fizz" , if the number is a multiple of 3
		Prints "Buzz", if the number is a multiple of 5
		Prints "FizzBuzz", if the number is a multiple of 3 and 5, i.e 15
		Prints "Prime", if the number is a prime number
		Otherwise, it prints the number
	Edge Case:
		3 is a prime number and will also generate "Fizz"
		Otherwise, any Fizz, Buzz or FizzBuzz cannot be a prime number
	'''
	for i in range(1,101):
		if i % 15 == 0:
			print("FizzBuzz")
		elif i % 5 == 0:
			print("Buzz")
		elif i % 3 == 0:
			print("Fizz")
			if i == 3: # take care of the edge case
				print("Prime")
		elif IsPrime(i) and i > 1:
			print("Prime")
		else:
			print(i)

		
		

def IsPrime(value):
	'''
	Checks if a given number is a prime number
	Returns:
		True - number is  a prime number
		False - number is not a prime number
	'''
	for i in range(2,value):
		if value % i ==0:
			return False
	return True

FizzBuzzPrime()
