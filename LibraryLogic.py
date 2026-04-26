# import required libraries like -> date, math....
from datetime import date
import math

# define init_library() function which initialize and returns Library Data like -> Books_records and issued_records....
def init_library():
    """Initializes and returns the library details and issue records."""
    # create a variable Books_records which stores books data in the form of dictionary....
    Books_records = {
        "B1": {"title": "Learn Python", "author": "Mark Lutz", "copies": 3},
        "B2": {"title": "Data Structures", "author": "Seymour Lipschutz", "copies": 2},
        "B3": {"title": "Algorithms", "author": "Thomas Cormen", "copies": 5}
    }
    # create variable issued_records which stores empty dictionary....
    issued_records = {} 
    # return variable Books_records and issued_records.... 
    return Books_records, issued_records

# define function issue_bweek = ((day - 1) // 7) + 1 
        # daily_charge = 10 * math.factorial(week)
        # total_fine += daily_chargeook() which takes parameters books_records, records, book_id, student_name, allotted_days.... 
def issue_book(books_records, records, book_id, student_name, allotted_days):
    # check if the book with the provided book_id is present inside the library or not....
    if book_id not in books_records:
        return "Book ID not found in books records."
    
    # check if the copy of book asked by the user is present inside books_records or not....
    if books_records[book_id]["copies"] <= 0:
        return "No copies available currently."
    
    # create id for issue book....
    issue_id = f"ISSUE-{len(records) + 1}"
    # deduct one copie of the book asked by the user.... 
    books_records[book_id]["copies"] -= 1
    
    # create and assign a dictionary object of new record of issued book inside issued records object....
    records[issue_id] = {
        "book_id": book_id,
        "student_name": student_name,
        "issue_date": date.today().strftime("%Y-%m-%d"),
        "allotted_days": allotted_days
    }

    # return successfull message with issue_id....
    return f"Book issued successfully! Your Issue ID is {issue_id}. Please save this."

# define function calculate_fine() which take parameter late_days to calculate fine....
def calculate_fine(late_days):
    """
    Calculates fine based on weeks late:
    Week 1: 10 * 1 = 10/day
    Week 2: 10 * 2 = 20/day
    Week 3: 10 * 2 * 3 = 60/day
    """
    # first checks if the late_days are less than or equals to 0.
    if late_days <= 0:
        return 0
    
    # create variable total_fine used to store fine....
    total_fine = 0
    for day in range(1, late_days + 1):
        print(day)
        # Calculate which week the late day falls into
        week = ((day - 1) // 7) + 1 
        daily_charge = 10 * math.factorial(week)
        total_fine += daily_charge
        
    return total_fine

# define function return_book() takes parameters books_data, records, issue_id, days_kept.... 
def return_book(books_data, records, issue_id, days_kept):
    # check if the records of issued book with the provided issue_id is present inside the issued_records.... 
    if issue_id not in records:
        return "Issue ID not found."

    # create variable record which stores value of those records whose issue_id is provided.... 
    record = records[issue_id]

    # create variable allotted_days which stores value of key allotted_days....
    allotted_days = record["allotted_days"]
    
    # create variable books_id which stores value of key book_id....
    book_id = record["book_id"]
    
    # if user kept book more than alloted days then fine will be imposed....
    late_days = days_kept - allotted_days
    fine = calculate_fine(late_days)
    
    # update the copie of issued book inside the Books_records.... 
    books_data[book_id]["copies"] += 1
    # delete the issued book records after the book is returned....
    del records[issue_id]
    
    # show the success message of returned book....
    message = f"Book returned successfully."
    
    # if calculate_fine() function returns fine....
    if fine > 0:
        message += f"\n[NOTICE] Book was {late_days} days late. A fine of Rs. {fine} has been applied."

    else:
        message += "\nBook Returned on time. No fine applied."

    # return message....
    return message

def AddBook(books_records, title, author, copies):
    length = 0
    
    for keys, values in books_records.items():
        length+=1
        # print(values['title'], values['author'], values['copies'])
        if(values['title']==title and values['author']==author):
            # print(f"book with {keys} is already present just update the copie with value of 1")
            # print(values['copies'])
            values['copies'] += 1

    book_id = f"B{length+1}"
    # print(book_id)
    books_records[book_id] = {
        book_id: {'title': title, 'author': author, 'copies': copies}
    }

    return "Book Successfully Added to the Library...."

def ShowBooks(books_records):
    for keys, values in books_records.items():
        print(keys, values)