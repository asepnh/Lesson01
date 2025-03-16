import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        user_input = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Sorry! You lost the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    play_game()