# Word Guess game

# Intro
This is my PP3 project to create a word guess game using Python. This runs using the code institute template and is deploted using Heroku. The goal is to guess the secret word before you run out of lives. The user can either guess a single letter or a 5 letter word. Once they guess the word, they will see their score. 
I took inspiration from Hangman and the popular game wordle to come up with this idea. 

Live game can be seen here - [Live Word Guess Game](https://jasonhorgan-pp3-4675d38d4f6d.herokuapp.com/)

## User Experience

### User Stories

As the creator of this site I want to create a game that is easy for users to understand, fun to play and also challenging but gives a sense of achievement when complete. 

As a first time visitor of the site I want to be able to easily understand what is going on, know where to find instructions if needed and feel compelled to come back and play again. 

As a returning visitor I want to be able to play the same game with a different word every time I play the game and feel a sense of accomplishment when I get the word right. 

## Design 

### Colour

There are colours used in the game text which are imported from the Colorama plugin. Green is used to display a correct letter or word guessed and red is used to represent an incorrect guess. Yellow is used to show the users score. 

### Flow Chart 

A flow chart was created using Lucid chart. This was my first time using LucidChart and although it took a little getting used to and I still feel I have a long way to go, this really helped me map out my project and break it down into easy to digest sections so I always knew what I needed to code next. 

## Features 

### Current Features

Welcome message:

A very basic welcome message where the user inputs their name to give the game a more personal feel 

img of intro

Instructions:

A brief paragraph explaining to the user the rules of the game and how to play with an option at the end to either start or quit the game

<>img of instructions

Main game loop:

The main game is a loop where the user can see how many lives they have and are prompted to enter a guess. The users guess needs to be either 1 letter or 5 letters in length.
if the letter is not in the word, they will see a message in red telling them the guess was wrong and will then deduct a life and tell them how many lives they have remaining. It will also then show them their current guesses. 

<>img of main game loop with wrong ans

If the user guesses a correct letter, they will see a green message telling them the letter they guessed is in the word and it will tell them the position of the letter in the word. They will not be deducted a life for guessing a correct letter. 

<>img of correct guess

This loop will continue until the user either guesses the word correctly or runs out of lives

<>img of run out of lives

<>img of won game

<>img of lose game

If the user wins or loses the game, they will be asked if they want to play again. 

Colorama is used to implement colours to make the game more visually appealing and indicate right answers, wrong answers, display the score and also show the user when they have entered an input that is not allowed. 

For input validation, I have included rules so that the user can only enter a guess that is 1 letter in length, 5 letters in length and only contains letters. If the user enters a guess that is more than 1 or 5 letters in length, or contains numbers or characters, they will be shown an error message and asked to input their guess again, as can be seen in the below screenshot. 

## Testing

### Manual testing

main menu:

- I entered letters symbols and numbers other than 1, 2 or 3
- entered nothing 
- entered symbols and numbers other than 1, 2 or 3
Result: As expected, error message in red text: Invalid choice, enter 1, 2 or 3 and then the loop runs again asking the user for an input

instructions:

- I entered letters symbols and numbers other than 1, 2 or 3
- entered nothing 
- entered symbols and numbers other than 1 or 2
Result: As expected, error message in red text: Invalid choice, enter 1, or 2 and then the loop runs again asking the user for an input.
if user selects 2: exits game with a message of "See you next time! "
if user selects 1: play game function executes

Play game:

- Enter nothing, a symbol or number, an empty space, a guess with a length of anything other than 1 or 5
Result: Error message prints in red "Guess must only contain letters " if guess is a syymbol. 
Error message in red : Guess can only be 1 or 5 letters in length: try again
Error message in red: 

<>img of screenshot

Restart:

- Enter anything other than Y or N
result: Error message in red "Invalid choice, enter Y or N " and then re run loop asking user for input

## PEP8 validator

PEP8 testing was completed using the CI linter programme - https://pep8ci.herokuapp.com/#
There were a few errors which I have cleaned up, mainly white spacing and trailing errors. 
My code runs through the linter programme with no errors now
<>img of linter ss

## User Testing

I had family and work colleague's test this to see if they could break it and all have thankfully been unsuccessful in breaking it so far.

##Python Libraries

The two libraries I used for this project was the random library to pull a random word from my word array each time the run game function runs so the user has a new experience each time they play the game. I also used Colorama to add some variety and nice visuals to the game. 

##Bugs

The main bug I dealt with during the writing of this code was that when a user entered a guess that contained  only 1 letter - if this letter was in the word, they would win the game. I fixed this by adding the condition that a guess needs to be 5 letters in length in order to win the game. 

# Future implementations

- I would like to implement easy, medium and hard modes which would include either more lives or different length words, depending on the difficulty selected. 
- I would like to implement a feature that prints back the guessed letter and the position. For example if the user guessed the letter 'a' and this was the second letter, they would see a printed statement saying: word so far: _ a _ _ _ .
- I would like to add a scoreboard that saves a users high score so people all over the world can play the game and compete for top spot on a leaderboard.

## Deployment

This project was deployed using Heroku and developed using the CI python template - https://github.com/Code-Institute-Org/p3-template

## Deployment procedure

- log into Heroku
- Create new app 
- choose an available name and region 
- as per love sandwiches walkthrough, config var with key PORT and 8000
- connect to github and deploy
- deploy early and then deploy finished code from heroku to ensure game is up to date on heroku with all code

# Credits 

https://www.youtube.com/watch?v=m4nEnsavl6w&t=526s - code for play game function referenced from this tutorial 

https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python - used this to figure out how to change an array to a string 

https://www.youtube.com/watch?v=u51Zjlnui4Y&t=464s - Colorama install tutorial

https://www.youtube.com/watch?v=LUWyA3m_-r0  - watched to help me understand and write User input validation 

https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response - watched to help me understand and write User input validation 

##Special Thanks

Special thanks to my mentor Graeme who helped and encouraged me throughout this project. He helped to keep me on track and instilled confidence in me by testing my knowledge of core concepts during our meetings. 
