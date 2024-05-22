import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import random 

#Variables

word = ["pause" , "train" , "their" , "chair" , "press"]

lives = 5

guesses = []

guessed_letter = []

guess = None

instructions = ""

user_score = None

username = None

start = None




def how_to_play():
    """
    prints game instructions
    """
    print("Welcome to the word guessing game\n")
    print("Your goal is to guess the word in the least amount of attempts\n")
    print("You can only guess a single letter or a 5 letter word\n")
    print("If your guess is not in the word, you lose a life\n")
    print("Keep making guesses until you get the word or run out of lives\n")
    print("Have fun!!!\n")


def main_menu():
    print("Welcome to the word guess game! \n")
    

    valid_choices = ('1' , '2' , '3')

    while True:
        start = input("Type 1 to start the game, 2 to see instructions or 3 to quit \n")

        if start not in valid_choices:
                print("Invalid choice, enter 1 or 2 \n")
        else: 
            break 

    if start == '1':
                play_game()
    elif start == '2':
                how_to_play()
    elif start =='3':
        print('See you next time! ')
    

def check_letter(secret_word , guess):
    print(Fore.GREEN + guess + " is in the word!")
    print("The letter was found at position " + str(secret_word.find(guess)+1))

def get_secret_word():
    secret_word = random.choice(word)
    return secret_word

def you_win(secret_word , guess , lives):
    if len(guess) == 5 and guess in secret_word:
            print(Fore.GREEN + "Congrats, you won! \n")
            print("The word was " + secret_word)
            user_score = lives*50
            print("You finished with " + str(lives) + " lives remaining \n")
            print("You scored " + str(user_score) + " points \n") 

def restart():
        print("Would you like to play again? \n")

        valid_choices = ('Y' , 'N')

        while True:
            start = input("Press Y to play again or N for main menu\n").upper()

            if start not in valid_choices:
                print("Invalid choice, enter Y or N \n")
            else: 
                break 

        if start == 'Y':
                play_game()
        elif start == 'N':
                main_menu()


def play_game():
    username = input("Please enter your username: \n") 
    print("Hi, " + username + " welcome to the word guess game! Good luck! \n")
    lives = 5
    secret_word = get_secret_word()
    guesses = []

    while lives > 0:
        print("number of lives remaining = " + str(lives))
        #guess = input("Please guess a word: \n").lower()

        while True: 
            guess = input("Please guess a word: \n").lower()

            if len(guess) >=2 and len(guess) <=4:
                print('Guess can only be single letter or 5 letter word, try again\n')
            
            elif len(guess) >=6 or not guess.isalpha():
                print('Guess can only be single letter or 5 letter word, try again\n')

            else:
                 break

        if guess not in secret_word:
            print(Fore.RED + "Wrong! Guess another letter or word \n")
            guesses.append(guess)
            lives -=1
            print("Words guessed so far: " + " , ".join(guesses))

        elif len(guess) == 1 and guess in secret_word:
            check_letter(secret_word , guess)
            guesses.append(guess)
            print("Words guessed so far: " + " , ".join(guesses))
        else:
            you_win(secret_word , guess , lives)
            restart()

            break

    if lives == 0:
        print("Unlucky! The word was " + secret_word)
        restart()
       



"""
def play_game():
    username = input("Please enter your username: \n") 
    print("Hi, " + username + " welcome to the word guess game! Good luck! \n")
    lives = 5
    secret_word = get_secret_word()
    guesses = []

    while lives > 0:
        print("number of lives remaining = " + str(lives))
        guess = input("Please guess a word: \n").lower()
        if guess not in secret_word:
            print(Fore.RED + "Wrong! Guess another word \n")
            guesses.append(guess)
            lives -=1
            print("Words guessed so far: " + " , ".join(guesses))

        elif len(guess) == 1 and guess in secret_word:
            check_letter(secret_word , guess)
            guesses.append(guess)
            print("Words guessed so far: " + " , ".join(guesses))
        else:
            you_win(secret_word , guess , lives)
            restart()

            break

    if lives == 0:
        print("Unlucky! The word was " + secret_word)
        restart()
 """      


main_menu()

