


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

# ask for a user input 

userchoice = input(" Please choose one: 'Rock', 'Paper', or 'Scissors'? ")
print("User chose", userchoice)

# validate the user input
if userchoice != "rock" or userchoice != "paper" or userchoice != "scissors":
     print("Please enter a valid input.")
     quit()
else:
    print("Opponent will now choose")

# computer choice
from random import choice
options = ["Rock","Paper","Scissors"]
computer_choice = choice(options)
print("Computer chose:", computer_choice)

# determine the winner


# display the final results 