from datetime import date
import math

def init_library():
    """Initializes and returns the library catalog and issue records."""
    Books_records = {
        "B1": {"title": "Learn Python", "author": "Mark Lutz", "copies": 3},
        "B2": {"title": "Data Structures", "author": "Seymour Lipschutz", "copies": 2},
        "B3": {"title": "Algorithms", "author": "Thomas Cormen", "copies": 5}
    }
    issued_records = {} 
    return Books_records, issued_records

def issue_book(books_records, records, book_id, student_name, allotted_days):
    if book_id not in books_records:
        return "Book ID not found in catalog."
    
    if books_records[book_id]["copies"] <= 0:
        return "No copies available currently."
        
    issue_id = f"ISSUE-{len(records) + 1}"
    books_records[book_id]["copies"] -= 1
    
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

def return_book(books_data, records, issue_id, days_kept):
    if issue_id not in records:
        return "Issue ID not found."
        
    record = records[issue_id]
    allotted_days = record["allotted_days"]
    book_id = record["book_id"]
    
    late_days = days_kept - allotted_days
    fine = calculate_fine(late_days)
    
    # Return to catalog and clean up
    books_data[book_id]["copies"] += 1
    del records[issue_id]
    
    message = f"Book returned successfully."
    if fine > 0:
        message += f"\n[NOTICE] Book was {late_days} days late. A fine of Rs. {fine} has been applied."
    else:
        message += "\nReturned on time. No fine applied."
        
    return message
