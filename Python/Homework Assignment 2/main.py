'''
Python Homework Assignment 2
Course: Python is Easy @ pirple
Author: Moosa
Email: gr8tech01@gmail.com

Use functions to list characteristics of my favourite song
'''

# Name of the artist
Artist = "Zain Bhikha"
# Artist official website
Website = "http://zainbhikha.com/"
# Favourite Song title
Song = "Forgive me when I whine"
# Song length in minutes:seconds
Duration = "2:35"
# Studio which produced album
Studio = "Zain Bhikha Studios"
# Language of the song
Language = "English"
# Title of Album
Album = "Mountains of Makkah"
# URL for Album details
Album_URL = "http://zainbhikha.com/album/08-mountains-of-makkah-2005/"
# Year album was released
Year = 2005
# Song genre
Genre = "Religion/R&B/Soul"
# URL for song video
Link = "https://www.youtube.com/watch?v=0TO4tWE3gSY"
# URL to Apple music store
itunes = "https://itunes.apple.com/us/album/336347122?i=336347257"
# Indicates if the song was perfomed by a single artist
Solo = True
# Lyrics for the song
Lyrics =  r'''
Today, upon a bus I saw a girl with golden hair,
And in my heart I wished that I was just as fair
When suddenly she rose to leave, I saw her hobble down the aisle.
She had one leg and wore a crutch, but as she passed, a smile.
Oh Allah Oh Allah , forgive me when I whine.
I have 2 legs to walk upon and the world is mine.

I stopped to buy some candy; i met a boy who had such charm.
We talked he seemed so happy, if I were late, it'd do no harm.
And as I left, he said to me, "Thank you, you've been so kind.
It's nice to talk with folks like you. You see," he said, "I'm blind."
Oh Allah Oh Allah , forgive me when I whine.
I have 2 eyes to see the world and the world is mine.

....
'''

def artist_name():
	'''
	Function returns the Artist Name
	'''
	return Artist

def song_title():
	'''
	Function returns the song title
	'''
	return Song

def year_released():
	'''
	Function returns the year song was released
	'''
	return Year

def is_solo():
	'''
	Functions indicates if the song was a Solo perfomance
	'''
	return Solo

# Testing the functions
print("Artist\t\t",artist_name())
print("Song\t\t",song_title())
print("Year\t\t",year_released())
print("Solo Perfomance\t",is_solo())