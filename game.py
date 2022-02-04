

#challenge 1- Environment variables 
import os

player_name = os.getenv("PLAYER_NAME", default="Player One")

print("----------")
print(f"Welcome {player_name} to my Rock-Paper-Scissors game!")
print("----------")
# ask for a user input 

userchoice = input(" Please choose one: 'Rock', 'Paper', or 'Scissors':")
print("User chose:", userchoice)

# validate the user input
userchoice = userchoice.lower()
if (userchoice == "rock") or (userchoice == "paper") or (userchoice == "scissors"):
     print("Opponent will now choose.")
else:
    print("Please chooose a valid input.")
    quit()

# computer choice
from random import choice
options = ["Rock","Paper","Scissors"]
computer_choice = choice(options)
print("Computer chose:", computer_choice)

print("----------")

# determine the winner
#Nikita's code that she posted in Slack helped me out!

computer_choice = computer_choice.lower()

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
