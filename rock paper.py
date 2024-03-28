import random

def get_user_choice():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def main():
    player_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"User chose: {user_choice}", end=" vs ")
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)
        if winner == "user":
            print("User wins this round!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a tie!")

        print(f"Player score: {player_score}", end=" | ")
        print(f"Computer score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()