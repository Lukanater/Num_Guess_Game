#This is the first major project, which is a number guessing game!

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    """
        Random number: rand.range(0,10)
        Random number: rand.range(0,10)
    """
    answer = 10
        #May change later, but for now I will make sure the answer pops up when it's guessed."
    answer = input(" ")
    print("WELCOME TO GUESS A NUMBER!!!!!!!!!!!!!!!!")
    guess = input("Choose a number between 1 and 10.")
    while guess:
        if guess > answer:
            print("Guess again! Go Lower!")
            
            
        elif guess < answer:
            print("Guess again! Go Higher!")
        else:
            print("You Win! This {} many tries it took you to guess the right number".format(guess))
            break
    # write your code inside this function.
    #This is second attempt at solving the problem.
    for guess_ans in guess:
        if guess > answer:
            print("Guess again! Go Lower!")
            
            
        elif guess < answer:
            print("Guess again! Go Higher!")
        else:
            print("You Win! This {} many tries it took you to guess the right number".format(guess))
            break

# Kick off the program by calling the start_game function.
start_game()