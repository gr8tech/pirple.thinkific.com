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
	'''
	for i in range(1,101):
		if i % 15 == 0:
			print(i,"FizzBuzz")
		elif i % 5 == 0:
			print(i,"Buzz")
		elif i % 3 == 0:
			print(i,"Fizz")
		if IsPrime(i):
			print(i,"Prime")

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
