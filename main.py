from datetime import date
import math

def init_library():
    """Initializes and returns the library catalog and issue records."""
    catalog = {
        "B001": {"title": "Learn Python", "author": "Mark Lutz", "copies": 3},
        "B002": {"title": "Data Structures", "author": "Seymour Lipschutz", "copies": 2},
        "B003": {"title": "Algorithms", "author": "Thomas Cormen", "copies": 5}
    }
    issued_records = {} # Format: {issue_id: {book_id, student_name, issue_date, allotted_days}}
    return catalog, issued_records

def issue_book(catalog, records, book_id, student_name, allotted_days):
    if book_id not in catalog:
        return False, "Book ID not found in catalog."
    
    if catalog[book_id]["copies"] <= 0:
        return False, "No copies available currently."
        
    issue_id = f"ISSUE-{len(records) + 1}"
    catalog[book_id]["copies"] -= 1
    
    records[issue_id] = {
        "book_id": book_id,
        "student_name": student_name,
        "issue_date": date.today().strftime("%Y-%m-%d"),
        "allotted_days": allotted_days
    }
    return True, f"Book issued successfully! Your Issue ID is {issue_id}. Please save this."

def calculate_fine(late_days):
    """
    Calculates fine based on weeks late:
    Week 1: 10 * 1 = 10/day
    Week 2: 10 * 2 = 20/day
    Week 3: 10 * 2 * 3 = 60/day
    """
    if late_days <= 0:
        return 0
        
    total_fine = 0
    for day in range(1, late_days + 1):
        # Calculate which week the late day falls into
        week = ((day - 1) // 7) + 1 
        daily_charge = 10 * math.factorial(week)
        total_fine += daily_charge
        
    return total_fine

def return_book(catalog, records, issue_id, days_kept):
    if issue_id not in records:
        return False, "Issue ID not found."
        
    record = records[issue_id]
    allotted_days = record["allotted_days"]
    book_id = record["book_id"]
    
    late_days = days_kept - allotted_days
    fine = calculate_fine(late_days)
    
    # Return to catalog and clean up
    catalog[book_id]["copies"] += 1
    del records[issue_id]
    
    message = f"Book returned successfully."
    if fine > 0:
        message += f"\n[NOTICE] Book was {late_days} days late. A fine of Rs. {fine} has been applied."
    else:
        message += "\nReturned on time. No fine applied."
        
    return True, message

import library_logic

def main():
    catalog, records = library_logic.init_library()
    
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
                    
                success, msg = library_logic.issue_book(catalog, records, b_id, s_name, days)
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
                success, msg = library_logic.return_book(catalog, records, issue_id, days_kept)
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

if __name__ == "__main__":
    main()