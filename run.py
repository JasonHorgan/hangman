import random 

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Variables

word = ["pause" , "train" , "their" , "chair" , "press"]

lives = 5

guesses = []

secret_word = random.choice(word) 

win = False

over = False

lose = False

instructions = ""

username = input('Welcome to Hangman! Please enter your username: ')

#print("Hello, " +username + "! Good luck in the game!")

def play_game(word):
    print(username) 
    lives = 5
    win = False
    
    while win==False:
        print("number of lives = " + str(lives))
        guess = input("Please guess a word: ")
        if guess in word:
            print("Congrats, you won!")
        else:
            print("Wrong! Guess another word")
            lives =-1
                
play_game(word)




print(secret_word)