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
    # write your code inside this function.
    print("WELCOME TO GUESS A NUMBER!!!!!!!!!!!!!!!!")
    answer = 10
    attempt = 1
        #May change later, but for now I will make sure the answer pops up when it's guessed."
    answer = input(" ")
    
    guess = input("Choose a number between 1 and 10.")
    #guess = int(input)
    guess = input(int)
    """while guess:
        if guess > answer:
            print("Guess again! Go Lower!"+guess)                        
                                
        elif guess < answer:
            print("Guess again! Go Higher!"+guess)
            
        else:
            print("You Win! This {} many tries it took you to guess the right number".format(guess))
            break"""
    #while guess:
    """for guess_ans in guess:
        if guess == answer:
            print("You Win! This {} many tries it took you to guess the right number".format(guess))         
            break
                                                                    
        elif guess > answer:
            print("Guess again! Go Lower!"+guess)
            
        elif guess < answer:
            print("Guess again! Go Higher!"+guess) """   
    while guess: 
        if guess == answer:
            print("You Win! This {} many tries it took you to guess the right number".format(attempt)) 
            attempt +=1
            break
                                                                    
        elif guess > answer:
            print("Guess again! Go Lower!")
            print (guess)
        elif guess < answer:
            print("Guess again! Go Higher!")
            print (guess)
# Kick off the program by calling the start_game function.
start_game()