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
    
number_guesses = 0  
high_score = [10, ]



    
def start_game():
  print("Welcome to the number guessing game!", "In this game, you will be prompted to guess a number, 1 through 10.", "Only use integers for your guesses, and try to guess the correct number randomly generated in as few guesses as possible.", "Good Luck!!!!")
  print("""
    TO GUESS A NUMBER, TYPE AN INTEGER WHEN PROMPTED
    
    THE HIGH SCORE IS CURRENTLY {} GUESSES.
  """.format(high_score[-1]))
  targetnum = random.randrange(1, 11)
  number_guesses = 1
  while True:
    try:
      guess = int(input("What number would you like to guess?  "))
      if guess < 1 or guess > 10:
        raise ValueError("That is not a valid value.  Please enter an integer between 1 and 10.")
    except ValueError:
      print("That is not a valid value.  Please enter an integer between 1 and 10.")
    else:
      if guess > targetnum:
          print("Incorrect, the number is lower!")
          number_guesses += 1
      elif guess < targetnum:
          print("Incorrect, the number is higher!")
          number_guesses += 1
      elif guess == targetnum:
        break
  print("That is Correct! You were able to guess the correct number in {} guesses.".format(number_guesses))
  if number_guesses < high_score[-1]:
    print("Congratulations, you've achieved a new HIGH SCORE!!!")
    high_score.append(number_guesses)
  replay = input("Would you like to play again?  [yes/no]  ")
  if replay == "yes":
    start_game()
  else:
    print("Thank you for playing!!!")
    print("High Scores:")
    for score in high_score:
      print("* ", score)
  

                   
  

# Kick off the program by calling the start_game function.
start_game()


