import random 

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Variables

word = ["pause" , "train" , "their" , "chair" , "press"]

lives = 5

guesses = []

guess = None

secret_word = random.choice(word) 

win = False

over = False

lose = False

instructions = ""

user_score = None

#username = input('Welcome to Hangman! Please enter your username: ')

username = None

#print("Hello, " +username + "! Good luck in the game!")

def play_game(secret_word):
    username = input("Please enter your username: ") 
    print("Hi, " + username + " welcome to the word guess game! Good luck!")
    lives = 5
    win = False
    
    while lives > 0:
        print("number of lives remaining = " + str(lives))
        guess = input("Please guess a word: ")
        if guess not in secret_word:
            print("Wrong! Guess another word")
            guesses.append(guess)
            lives -=1
            print("Words guessed so far: " + " , ".join(guesses))
        else:
            print("Congrats, you won!")
            user_score = lives*50
            print("You finished with " + str(lives) + " lives remaining")
            print("You scored " + str(user_score) + " points")
            break

            
                
play_game(secret_word)




print(secret_word)