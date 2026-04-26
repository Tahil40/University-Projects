# import PlayStonePaperScissor function from game_logic file....
from game_logic import PlayStonePaperScissor

# define main function which executes main logic of the game using while loop....
def main():
    while True:
        print("\n" + "*"*30)
        print("       ARCADE ZONE")
        print("*"*30)
        print("1. Play Stone - Paper - Scissors")
        print("2. Exit")
        print("*"*30)
        
        # take input from the user....
        choice = input("Choose an option (1-2): ")
        
        # if the user input 1 the it means user want to play game then execute PlayStonePaperScissor function.... 
        if choice == '1':
            print("\n--- Stone, Paper, Scissors ---")
            try:
                # convert user's input into lowercase() and then remove extra spaces using .strip() function....
                user_input = input("Enter 'stone', 'paper', or 'scissors': ").lower().strip()

                # create variables computer_choice, result which stores computer_choice and result return by PlayStonePaperScissor function....
                computer_choice, result = PlayStonePaperScissor(user_input)
                
                # if PlayStonePaperScissor return result "Invalid choice" then show it to user using print() function....
                if result == "Invalid choice!":
                    print("=> Invalid choice. Please try again.")

                else:
                    print(f"Computer choose: {computer_choice.capitalize()}")
                    print(f"Result: {result}")

            except Exception:
                print("\n=> Error; choose valid option")

        if choice == '2':
            break

main()