


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

print("----------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game!")
print("----------")
# ask for a user input 

userchoice = input(" Please choose one: 'Rock', 'Paper', or 'Scissors':")
print("User chose:", userchoice)

# validate the user input
userchoice = userchoice.lower()
if (userchoice != "rock") or (userchoice != "paper") or (userchoice != "scissors"):
     print("Please enter a valid input.")
     quit()
else:
    print("Opponent will now choose")

# computer choice
from random import choice
options = ["Rock","Paper","Scissors"]
computer_choice = choice(options)
print("Computer chose:", computer_choice)

print("----------")

# determine the winner
#Nikita's code that she posted in Slack helped me out!
def determine_the_winner(userchoice, computer_choice):
    #user chose paper
    if userchoice == "paper" and computer_choice == "rock":
        print("You are the winner! :)")
    elif userchoice == "paper" and computer_choice == "scissors":
        print("You lost! :(")
    elif userchoice == "paper" and computer_choice == "paper":
        print("It's a tie! :D")
    
    #user chooses scissors
    if userchoice == "scissors" and computer_choice == "rock":
        print("You lost! :(")
    elif userchoice == "scissors" and computer_choice == "scissors":
        print("It's a tie! :D")
    elif userchoice == "scissors" and computer_choice == "paper":
        print("You are the winner! :)")

    #user chooses rock
    if userchoice == "rock" and computer_choice == "rock":
        print("It's a tie! :D")
    elif userchoice == "rock" and computer_choice == "scissors":
        print("You are the winner! :)")
    elif userchoice == "rock" and computer_choice == "paper":
        print("You lost! :(")

print("----------")

# display the final results 
print("Thank you for playing the game! Please play again!")
