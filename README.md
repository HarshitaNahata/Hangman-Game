# Hangman-Game
The Hangman game is a simple guessing game where the computer chooses a random word and the player tries to guess the letters in the word one at a time. The player has a limited number of incorrect guesses before the game is over.


The game can be implemented in Python in a few simple steps:

Import the random module.
Create a list of words to choose from.
Choose a random word from the list.
Initialize a variable to keep track of the number of incorrect guesses.
Create a loop that continues until the player has guessed the word or has reached the maximum number of incorrect guesses.
In each iteration of the loop, ask the player to guess a letter.
If the letter is in the word, update the list of guessed letters and remove the letter from the word.
If the letter is not in the word, increment the number of incorrect guesses.
If the number of incorrect guesses reaches the maximum, the player loses the game.
If the player guesses the word, the player wins the game.
