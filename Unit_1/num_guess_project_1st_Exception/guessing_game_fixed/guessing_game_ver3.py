
#This is the first major project, which is a number guessing game!
#This is an alternative version of the previous project to try another new approach.
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import random



#defing variable for reflecting random range; which would be used to check if the number is the right number between a range of numbers

"""This is for how many tries it will take the player to guess what the answer is.
    When the player has gotten the right number, the number of attempts will be shown. 
    Attempt will increase before someone gets the right "answer"."""


#guess = int()
def begin_game():
    
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
    print("WELCOME TO GUESS A NUMBER!!!!!!!!!!!!!!!!")
    print("-------------This is Guess a number!!!!!!!!!! Get ready, set, go!-------------")
    
    answer = random.randint(0,20)
    
    
    attempt = 1
    #Need to raise an exception of types, and characters, so the player is reminded to only guess a number.
    #Need to raise an exception of number range, so the player is reminded to only guess withen that range.
    while True:
        guess = input("Guess a number between 0 and 20.")
        guess = int(guess)
        if guess > answer:
            print("Go lower!")
            print(guess)
            attempt+=1
            
            
        elif guess < answer:
            print("Go higher!")
            print(guess)
            attempt+=1
            
            
        else:
            print("You win! This is how many attempts it took you to guess the right number: {}".format(attempt))
            attempt +=1
            
            print("Thanks for playing GUESS A NUMBER!!! It was swell having you on this show!")
            break
play_again = input("Do you want to play again? Yes or No?")
#Yes = "Yes"
#No = "No"
#Now the game ends. There will be later, an option if the player would like to play again!
begin_game()