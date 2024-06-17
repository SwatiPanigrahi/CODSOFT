import random

while True:
    print("Enter your choice: rock(R), paper(P), or scissor(S)")
    user_choice = input ("Your choices: ")
    possible_choices = ["R", "P", "S"]
    computer_choice = random.choice(possible_choices)
    

    if user_choice == computer_choice:
       print(f"Both players chose {user_choice}. It's a tie!")


    elif user_choice == "R":
     if computer_choice == "S":
        print("Rock beats scissors! You win.")
     else:
        print("Paper beats rock! You lose.")


    elif user_choice == "P":
     if computer_choice == "R":
        print("Paper beats rock! You win.")
     else:
        print("Scissor beats paper! You lose.")


    elif user_choice == "S":
     if computer_choice == "P":
        print("Scissor beats paper! You win.")
     else:
        print("Rock beats scissor! You lose.")


    play_again = input("Want to play again?")
    if play_again.lower() != "Yes":
     print("Yes")
    else:
     print("Exit")