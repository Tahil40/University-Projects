from ATM_logic import initialize_account, get_balance, withdraw, deposit, get_transactions

def main():
    # create account variable which stores bank details like balance and transactions returned by initialize_account() function....
    account = initialize_account()
    
    while True:
        print("\n" + "="*30) #first retuns new line and then prints = sign 30 times....
        print("     WELCOME TO THE ATM")
        print("="*30)
        print("1. Display Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Get Transactions")
        print("5. Exit")
        print("="*30)
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print(f"\n=> Current Balance: Rs. {get_balance(account):.2f}")
            
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: Rs. "))
                message = withdraw(account, amount)
                print(f"\n=> {message}")
                
            except Exception:
                print("\n=> Invalid input! Please enter a valid number.")
                
        elif choice == '3':
            try:
                amount = float(input("Enter amount to deposit: Rs. "))
                message = deposit(account, amount)
                print(f"\n=> {message}")

            except Exception:
                print("\n=> Invalid input! Please enter a valid number.")
                
        elif choice == '4':
            print("\n--- Account Transactions ---")
            statement = get_transactions(account)
            if not statement:
                print("No transactions yet.")
            else:
                for record in statement:
                    print(record)
            print("-------------------------")
            
        elif choice == '5':
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print("\n=> Invalid choice! Please select an option from 1 to 5.")
main()