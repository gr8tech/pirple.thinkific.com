'''
Python Homework Assignment 9
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

OOP - Classes
'''
import random

class Vehicle:
	'''
	Represents the Vehicle class
	'''
	def __init__(self, Make="", Model="", Year=1900, Weight=0):
		'''
		Initialize object with some defaults
		'''
		self.Make = Make
		self.Model = Model
		self.Year = Year
		self.Weight = Weight
		self.NeedsMaintanace = False
		self.TripsSinceMaintanance = 0

	def setMake(self, Make):
		'''
		Sets the Make of vehice
		'''
		self.Make = Make

	def setModel(self, Model):
		'''
		Sets the Model of vehice
		'''
		self.Model = Model

	def setYear(self, Year):
		'''
		Sets the Year of vehice manufacture
		'''
		self.Year = Year

	def setWeight(self, Weight):
		'''
		Set vehicle weight in kgs
		'''
		self.Weight = Weight

	def Repair(self):
		'''
		After repair, reset counters
		'''
		self.TripsSinceMaintanance = 0
		self.NeedsMaintanace = False

class Cars(Vehicle):
	'''
	Represents the Cars class. Inherits from the Vehicles class
	'''
	def __init__(self, Make="", Model="", Year=1900, Weight=0):
		'''
		Initialize object with some defaults
		'''
		Vehicle.__init__(self,Make, Model, Year, Weight)
		self.isDriving = False

	def Drive(self):
		'''
		Drive the car
		'''
		self.isDriving = True

	def Stop(self):
		'''
		Stop the car
		'''
		if self.isDriving:
			self.isDriving = False
			# increment trip counter
			self.TripsSinceMaintanance += 1
			if self.TripsSinceMaintanance > 100:
				# Car needs maintanance after 100 trips
				self.NeedsMaintanace = True

class Planes(Vehicle):
	
	def __init__(self,Make="", Model="", Year=1900, Weight=0):
		'''
		Initialize object with some defaults
		'''
		Vehicle.__init__(self,Make, Model, Year, Weight)
		self.isFlying = False

	def Flying(self):
		'''
		Fly the plane
		Returns:
			True - plane can fly
			False - plane is due for service and cannot fly
		'''
		if self.NeedsMaintanace:
			print("The plane can't fly until it has been repaired")
			return False
		else:
			self.isFlying = True
			return True

	def Landing(self):
		'''
		Land the plane
		'''
		if self.isFlying:
			self.isFlying = False
			# increment trip counter
			self.TripsSinceMaintanance += 1
			if self.TripsSinceMaintanance == 100:
				# plane is due for service after 100 trips
				self.NeedsMaintanace = True

def TestDrive(vehicle):
	'''
	Test the vehicle and output vehicle characteristics and 
	trip counters
	'''
	# randomly pick number of trips
	trips = random.randint(50,150)

	if type(vehicle) == Planes:
		for _ in range(trips):
			if not vehicle.Flying():
				break
			vehicle.Landing()
	elif type(vehicle) == Cars:
		for _ in range(trips):
			vehicle.Drive()
			vehicle.Stop()		

	print("{:<28s} {}".format("Make",vehicle.Make))
	print("{:<28s} {}".format("Model",vehicle.Model))
	print("{:<28} {}".format("Year",vehicle.Year))
	print("{:<28s} {}".format("Weight",vehicle.Weight))
	print("{:<28s} {}".format("Needs Maintanance",vehicle.NeedsMaintanace))
	print("{:<28s} {}".format("Trips Since Maintanance",
								vehicle.TripsSinceMaintanance))
	print()

if __name__ == "__main__":
	corolla = Cars()
	corolla.setMake("Toyota")
	corolla.setModel("Corolla")
	corolla.setYear(2002)
	corolla.setWeight(1165)

	sunny = Cars()
	sunny.setMake("Nissan")
	sunny.setModel("Sunny")
	sunny.setYear(2003)
	sunny.setWeight(1080)	

	chev = Cars()
	chev.setMake("Chevrolet")
	chev.setModel("Cruze")
	chev.setYear(2018)
	chev.setWeight(1387)	

	boeing = Planes("Boeing","787 Dreamliner",2018,161000)
	boeing.setMake("Boeing")
	boeing.setModel("787 Dreamliner")
	boeing.setYear(2018)
	boeing.setWeight(161000)	
	
	TestDrive(corolla)
	TestDrive(sunny)
	TestDrive(chev)
	TestDrive(boeing)


