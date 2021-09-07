import random

while True:

    choice = input("Enter a chocie, Rock, Paper, or Scissors: ").lower()

    possable_actions = ['rock', 'paper', 'scissors']
    computer_action = random.choice(possable_actions)

    print(f"\nyou chose {choice}, computor chose {computer_action}.\n")

    if choice == computer_action:
            print(f"Both players selected {choice}. Its a tie!")
    elif choice == 'rock':
        if computer_action == 'scissors':
            print("Rock beats Scissors! Computer lost")
        else:
            print("Paper beats Rock! Computer wins")
    elif choice == 'paper':
        if computer_action == 'rock':
            print("Paper beats Rock! Computer lost")
        else:
            print("Scissors beats Paper! Computer won")
    elif choice == 'scissors':
        if computer_action == 'paper':
            print("Scissors beat Paper! Computer lost")
        else:
            print("Rock beats Scissors! Computer won")

    play_again = input("Play again (y/n): ")
    if play_again.lower() != 'y':
        break