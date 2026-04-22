
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

    main()