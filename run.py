import random 

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Variables

word = ["pause" , "train" , "their" , "chair" , "press"]

lives = 5

guesses = []

secret_word = None 

win = False

over = False

lose = False

instructions = ""

username = input('Welcome to Hangman! Please enter your username: ')

print("Hello, " +username + "! Good luck in the game!")