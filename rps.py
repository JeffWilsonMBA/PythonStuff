# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if computer_choice == user_choice:
    print(str(computer_choice) + "!  Draw!")

elif computer_choice == "r" and user_choice == "s": 
    print("The computer chose rock and you chose scissors.")
    print("Rock breaks scissors.  The computer won!")

elif computer_choice == "s" and user_choice == "p":
    print("The computer chose scissors and you chose paper.")
    print("Scissors cut paper.  The computer won!")

elif computer_choice == "p" and user_choice == "r":
    print("The computer chose paper and you chose rock.")
    print("Paper covers rock.  The computer won!")

elif user_choice == "r" and computer_choice == "s": 
    print("You chose rock and the computer chose scissors.")
    print("Rock breaks scissors.  The computer won!")

elif user_choice == "s" and computer_choice == "p":
    print("You chose scissors and the computer chose paper.")
    print("Scissors cut paper.  The computer won!")

elif user_choice == "p" and computer_choice == "r":
    print("You chose paper and the computer chose rock.")
    print("Paper covers rock.  The computer won!")
else:
    pass
    