# introduces conditionals, lists, importing from the std lib and string interpolation

import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice = input("Do you want rock, paper or scissors?\n")

if computer_choice == user_choice:
    print("DRAW!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("{0} beats {1}, YOU WIN!".format(user_choice, computer_choice))
elif user_choice == "paper" and computer_choice == "rock":
    print("{0} beats {1}, YOU WIN!".format(user_choice, computer_choice))
elif user_choice == "scissors" and computer_choice == "paper":
    print("{0} beats {1}, YOU WIN!".format(user_choice, computer_choice))
else:
    print("{0} beats {1}, YOU LOSE :(".format(computer_choice, user_choice))
