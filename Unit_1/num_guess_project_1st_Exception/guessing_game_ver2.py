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
    attempt = 1
    answer = 10
    guess = int()
    guess = input("Choose a number between 1 and 10.")
        #May change later, but for now I will make sure the answer pops up when it's guessed."
    answer = input(" ")
    while guess:
        try:
              if guess > answer:
                  print("Go lower!")
              
              elif guess < answer:
                  print("Go higher!")
            
            
        except:  
              if guess == answer:
              #else:
                  print("You win! This is how many attempts it took you to guess the right number: {}".format(attempt))
                  attempt +=1
        break
    # write your code inside this function.
    #This is second attempt at solving the problem.
"""    for guess_ans in guess:
        if guess > answer:
            print("Guess again! Go Higher!")
            
            
        elif guess < answer:
            print("Guess again! Go Lower!")
        else:
            print("You Win! This {} many tries it took you to guess the right number".format(attempt))
            attempt+=1
            break"""

# Kick off the program by calling the start_game function.
start_game()