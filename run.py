import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
# Variables
STARTING_LIVES = 5
word = ["pause", "train", "their", "chair", "alone",
        "arise", "brain", "court", "doubt", "entry",
        "fruit", "grade", "ghost", "horse", "knife",
        "learn", "large", "movie", "media", "noise",
        "newly", "ocean", "often", "phone", "place",
        "power", "pitch", "quiet", "quick", "relax",
        "rapid", "ready", "stare", "sound", "smart"
        "stake", "shrug", "space", "shine", "scope",
        "shock", "trend", "thing", "thick", "thank",
        "under", "urban", "vital", "video", "voice",
        "waste", "woman", "works", "youth", "young"]


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
    valid_choices = ("1", "2")
    while True:
        start = input("Type 1 to start the game or 2 to quit \n")
        if start not in valid_choices:
            print("Invalid choice, enter 1 or 2 \n")
        else:
            break
    if start == "1":
        play_game()
    elif start == "2":
        print("See you next time! ")


def main_menu():
    print("Welcome to the word guess game! \n")
    global username
    username = input("Please enter your username: \n")
    valid_choices = ("1", "2", "3")
    while True:
        start = input("Type 1 to start game, 2 for instructions, 3 to quit \n")
        if start not in valid_choices:
            print(Fore.RED + "Invalid choice, enter 1 or 2 \n")
        else:
            break
    if start == "1":
        play_game()
    elif start == "2":
        how_to_play()
    elif start == "3":
        print("See you next time! ")


def check_letter(secret_word, guess):
    print(Fore.GREEN + guess + " is in the word!")
    print("Letter was found at position " + str(secret_word.find(guess) + 1))


def get_secret_word():
    secret_word = random.choice(word)
    return secret_word


def you_win(secret_word, guess, lives):
    if len(guess) == 5 and guess in secret_word:
        print(Fore.GREEN + "Congrats, you won! \n")
        print("The word was " + Fore.GREEN + secret_word)
        user_score = lives * 50
        print("You finished with " + str(lives) + " lives remaining \n")
        print("You scored " + Fore.YELLOW + str(user_score) + " points \n")


def restart():
    print("Would you like to play again? \n")
    valid_choices = ("Y", "N")
    while True:
        start = input("Press Y to play again or N to quit\n").upper()
        if start not in valid_choices:
            print(Fore.RED + "Invalid choice, enter Y or N \n")
        else:
            break
    if start == "Y":
        play_game()
    elif start == "N":
        print("Ok, see you next time! ")


def play_game():
    """
    input explanation
    """
    print("Hi, " + username + " welcome to the word guess game! Good luck! \n")
    lives = STARTING_LIVES
    secret_word = get_secret_word()
    guesses = []
    while lives > 0:
        print("number of lives remaining = " + str(lives))
        while True:
            guess = input("Please guess a letter or word: \n").lower()
            if len(guess) >= 2 and len(guess) <= 4:
                print(
                    Fore.RED
                    + "Guess can only be 1 or 5 letters in length: try again\n"
                )
            elif len(guess) >= 6:
                print("Guess must only be 5 letter in length \n")
            elif not guess.isalpha():
                print(Fore.RED + "Guess must only contain letters ")
            else:
                break
        if guess not in secret_word:
            print(Fore.RED + "Wrong! Guess another letter or word \n")
            guesses.append(guess)
            lives -= 1
            print("Words guessed so far: " + " , ".join(guesses))
        elif len(guess) == 1 and guess in secret_word:
            check_letter(secret_word, guess)
            guesses.append(guess)
            print("Words guessed so far: " + " , ".join(guesses))
        else:
            you_win(secret_word, guess, lives)
            restart()
            break
    if lives == 0:
        print("Unlucky! The word was " + Fore.RED + secret_word)
        restart()


if __name__ == "__main__":
    main_menu()
