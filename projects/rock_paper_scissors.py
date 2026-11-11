# Project 1: Rock, Paper, Scissors
# You want to create a simple game of Rock-Paper-Scissors in Python that takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.

# User input function to get the user's choice
def get_user_choice():
    # Get the user's choice of Rock, Paper, or Scissors
    user_input = input("Enter your choice (Rock, Paper, Scissors): ").strip().lower()
    if user_input in ['rock', 'paper', 'scissors']:
        return user_input
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()

# Main function to handle the game logic
def main():
    import random

    # Define the choices
    choices = ['rock', 'paper', 'scissors']

    # Get the user's choice
    user_choice = get_user_choice()

    # Get the computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")     

if __name__ == "__main__":
    main()  
