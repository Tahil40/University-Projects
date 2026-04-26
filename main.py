from LibraryLogic import init_library, issue_book, return_book, ShowBooks, AddBook

def main():
    books_records, issued_records = init_library()
    
    while True:
        print("\n" + "="*50)
        print("          LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("  1. View Available Books")
        print("  2. Issue a Book")
        print("  3. Return a Book")
        print("  4. View Library Fine Structure")
        print("  5. Add Book")
        print("  6. Exit")
        print("="*50)
        
        choice = input("\nSelect an operation (1-5): ")
        
        if choice == '1':
            print("\n--- Available Books in Library ---\n")
            ShowBooks(books_records)
                
        elif choice == '2':
            print("\n--- Issue Book Portal ---")
            b_id = input("Enter Book ID to issue: ").strip().upper()
            s_name = input("Enter Student Name: ").strip().title()
            
            try:
                days = int(input("Enter number of days book is issued for: "))
                if days <= 0:
                    print("=> Days must be greater than 0.")
                    continue
                    
                message = issue_book(books_records, issued_records, b_id, s_name, days)
                print(f"\n=> {message}")

            except ValueError:
                print("=> Invalid input! Please enter a valid number for days.")
                
        elif choice == '3':
            print("\n--- Return Book Portal ---")
            issue_id = input("Enter your Issue ID: ").strip().upper()
            
            try:
                days_kept = int(input("How many days did you keep the book in total? "))
                message = return_book(books_records, issued_records, issue_id, days_kept)
                print(f"\n=> {message}")
            except ValueError:
                print("=> Invalid input! Please enter a valid number of days.")
                
        elif choice == '4':
            print("\n--- Fine Structure Rules ---")
            print("If a book is returned after the allotted days, fines apply dynamically:")
            print(" * 1st Week late : Rs. 10 per day")
            print(" * 2nd Week late : Rs. 20 per day (10 * 2)")
            print(" * 3rd Week late : Rs. 60 per day (10 * 2 * 3)")
            
        elif choice == '5':
            print("\n--- Add Book Portal ---")
            book_title = input("Enter The Book Name; ").strip().title()
            book_author = input("Enter The Book Author; ").strip().title()
            copies = int(input("Enter The Number of Copies; "))
            message = AddBook(books_records, title=book_title, author=book_author, copies=copies)
            print(f"\n=>{message}")
        
        elif choice == '6':
            print("\nShutting down Library Management System. Goodbye!")
            break
            
        else:
            print("\n=> Invalid selection! Please choose a valid menu number.")
        
main()