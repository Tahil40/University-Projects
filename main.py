from LibraryLogic import init_library, issue_book, return_book

def main():
    catalog, records = init_library()
    
    while True:
        print("\n" + "="*50)
        print("          LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("  1. View Available Books")
        print("  2. Issue a Book")
        print("  3. Return a Book")
        print("  4. View Library Rules & Fine Structure")
        print("  5. Exit")
        print("="*50)
        
        choice = input("\nSelect an operation (1-5): ")
        
        if choice == '1':
            print("\n--- Available Book Catalog ---")
            print(f"{'ID':<6} | {'Title':<20} | {'Author':<18} | {'Copies':<5}")
            print("-" * 55)
            for b_id, details in catalog.items():
                print(f"{b_id:<6} | {details['title']:<20} | {details['author']:<18} | {details['copies']:<5}")
                
        elif choice == '2':
            print("\n--- Issue Book Portal ---")
            b_id = input("Enter Book ID to issue (e.g., B001): ").strip().upper()
            s_name = input("Enter Student Name: ").strip().title()
            
            try:
                days = int(input("Enter number of days book is issued for: "))
                if days <= 0:
                    print("=> Days must be greater than 0.")
                    continue
                    
                msg = issue_book(catalog, records, b_id, s_name, days)
                print(f"\n=> {msg}")
            except ValueError:
                print("=> Invalid input! Please enter a valid number for days.")
                
        elif choice == '3':
            print("\n--- Return Book Portal ---")
            issue_id = input("Enter your Issue ID (e.g., ISSUE-1): ").strip().upper()
            
            # For testing purposes, we ask the user how many days they actually kept it.
            # In a real system, this would be calculated automatically using datetime.
            try:
                days_kept = int(input("How many days did you keep the book in total? "))
                msg = return_book(catalog, records, issue_id, days_kept)
                print(f"\n=> {msg}")
            except ValueError:
                print("=> Invalid input! Please enter a valid number of days.")
                
        elif choice == '4':
            print("\n--- Fine Structure Rules ---")
            print("If a book is returned after the allotted days, fines apply dynamically:")
            print(" * 1st Week late : Rs. 10 per day")
            print(" * 2nd Week late : Rs. 20 per day (10 * 2)")
            print(" * 3rd Week late : Rs. 60 per day (10 * 2 * 3)")
            print(" * 4th Week late : Rs. 240 per day (10 * 2 * 3 * 4)")
            print("... and so on.")
            
        elif choice == '5':
            print("\nShutting down Library Management System. Goodbye!")
            break
            
        else:
            print("\n=> Invalid selection! Please choose a valid menu number.")
        
main()