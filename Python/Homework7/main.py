'''
Python Homework Assignment 7
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

Use a dictionary to store characteristics of my favourite song
'''

# Dictionary to hold song characteristics
Song = dict()
# Name of the artist
Song["Artist"] = "Zain Bhikha"
# Artist official website
Song["Website"] = "http://zainbhikha.com/"
# Favourite Song title
Song["Title"] = "Forgive me when I whine"
# Song length in minutes:seconds
Song["Duration"] = "2:35"
# Studio which produced album
Song["Studio"] = "Zain Bhikha Studios"
# Language of the song
Song["Language"] = "English"
# Title of Album
Song["Album"] = "Mountains of Makkah"
# URL for Album details
Song["Album_URL"] = "http://zainbhikha.com/album/08-mountains-of-makkah-2005/"
# Year album was released
Song["Year"] = 2005
# Song genre
Song["Genre"] = "Religion/R&B/Soul"
# URL for song video
Song["Video"]= "https://www.youtube.com/watch?v=0TO4tWE3gSY"
# URL to Apple music store
Song["itunes"] = "https://itunes.apple.com/us/album/336347122?i=336347257"
# Lyrics for the song
Song["Lyrics"] =  "http://lyrics.wikia.com/wiki/Zain_Bhikha:Forgive_Me_When_I_Whine"


def GuessCharacteristic(Key, Value):
	'''
	Guess the charactristic of a Song, by providing the Characteristic and its Value
	Args:
		Key - Song Characteristic
		Value - Value of the Characteristic
	Returns:
		True - Both the Key and Value are correct
		False - Otherwise
	'''
	if (Key in Song) and (Song[Key] == Value):
		return True
	else:
		return False

# print the value of the Song dictionary for every key present
for key, value in Song.items():
	print("{:<10s} : {}".format(key, value))

#  Testing
print(GuessCharacteristic("Artist","Zain Bhikha")) # True
print(GuessCharacteristic("Year",2005)) # True
print(GuessCharacteristic("Year",2010)) # False
print(GuessCharacteristic("Years",2005)) # False
