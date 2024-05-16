import random 

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Variables

word = ["pause" , "train" , "their" , "chair" , "press"]

lives = 5

guesses = []

guessed_letter = []

guess = None

win = False

over = False

lose = False

instructions = ""

user_score = None

#username = input('Welcome to Hangman! Please enter your username: ')

username = None

#print("Hello, " +username + "! Good luck in the game!")

def check_letter(secret_word , guess):
    print( guess + " is in the word!")
    print("The letter was found at position " + str(secret_word.find(guess)+1))

def get_secret_word():
    secret_word = random.choice(word)
    return secret_word

def play_game():
    username = input("Please enter your username: ") 
    print("Hi, " + username + " welcome to the word guess game! Good luck!")
    lives = 5
    win = False
    secret_word = get_secret_word()
    
    while lives > 0:
        print("number of lives remaining = " + str(lives))
        guess = input("Please guess a word: ")
        if guess not in secret_word:
            print("Wrong! Guess another word")
            guesses.append(guess)
            lives -=1
            print("Words guessed so far: " + " , ".join(guesses))

        elif len(guess) == 1 and guess in secret_word:
            check_letter(secret_word , guess)
            guesses.append(guess)
            print("Words guessed so far: " + " , ".join(guesses))
        else:
            print("Congrats, you won!")
            print("The word was " + secret_word)
            user_score = lives*50
            print("You finished with " + str(lives) + " lives remaining")
            print("You scored " + str(user_score) + " points")
            break

    if lives == 0:
        print("Unlucky! The word was" + secret_word)


   

play_game()
