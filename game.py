


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

# ask for a user input 

userchoice = input(" Please choose one: 'Rock', 'Paper', or 'Scissors'? ")
userchoice.lower
print("User chose", userchoice)

# validate the user input
if userchoice.lower != "rock" or "paper" or "scissors":
    print("Please enter a valid input.") and quit()

# computer choice
import random
options = ["Rock","Paper","Scissors"]
computer_choice = random.choice(options)
print("Computer chose:", computer_choice)

# determine the winner

# display the final results 