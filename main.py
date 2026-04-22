import random

def play_rps(user_choice):
    """Logic for Stone - Paper - Scissors"""
    choices = ['stone', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    if user_choice not in choices:
        return None, computer_choice, "Invalid choice!"
        
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You Win!"
    else:
        result = "Computer Wins!"
        
    return computer_choice, result

import game_logic

def main():
    while True:
        print("\n" + "*"*30)
        print("       ARCADE ZONE")
        print("*"*30)
        print("1. Play Stone - Paper - Scissors")
        print("2. Play Dice Roll Game")
        print("3. Exit")
        print("*"*30)
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            print("\n--- Stone, Paper, Scissors ---")
            user_input = input("Enter 'stone', 'paper', or 'scissors': ").lower().strip()
            
            comp_choice, result = game_logic.play_rps(user_input)
            
            if result == "Invalid choice!":
                print("=> Invalid choice. Please try again.")
            else:
                print(f"Computer chose: {comp_choice.capitalize()}")
                print(f"Result: {result}")

if __name__ == "__main__":
    main()