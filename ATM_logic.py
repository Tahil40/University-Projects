# import datetime library.... 
from datetime import datetime 

# create a function initialize_account() which set the initial bank details....
def initialize_account():
    """Returns a dictionary variable named bank_account representing the user's account state."""
    bank_account = {
        "balance": 0.0,
        "transactions": []
    }
    return bank_account

# create a function get_balance() which take parameter account and return bank balance....
def get_balance(account):
    # accessing value of key balance using account parameter....
    return account["balance"]

# create a function record_transaction which saves the record of transactions made by the user....
def record_transaction(account, amount_type, amount):
    # create variable timestamp which stores the timestamp of time when the transaction is made by the user....
    '''
    datetime.now() function returns the current date with time and .strftime() function converts that date and time into the format passed as an parameter into the .strftime() 
    like -> %Y -> returns year, %m -> returns month, %d -> returns day, %H -> returns hours, %M -> returns minutes and %S -> returns seconds.
    '''
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"[{timestamp}] {amount_type}: Rs. {amount:.2f} | Balance: Rs. {account['balance']:.2f}"
    # adding records into the transactions list....
    account["transactions"].append(record)

# create a function name deposit which takes two parameters 
def deposit(account, amount):
    # checks if the amount's value is greater than 0 because amount cannot be negative....
    if amount > 0:
        # update the value of balance by adding amount given by the user into the user's balance....
        account["balance"] += amount
        # calling record_transaction function to record the into the user's account....
        record_transaction(account, "Deposit", amount)
        return f"Successfully deposited Rs. {amount:.2f}"
    
    # check if the amount enter by the user is less or equals to zero then show error message to the user....
    if amount <= 0:
        return "Deposit amount must be strictly positive and cannot be Zero."

# create a function withdraw which takes 2 parameters account and amount 
def withdraw(account, amount):
    # checks is the amount enter by the user is less than or equals to 0 or not if yes then return error message to the user....
    if amount <= 0:
        return "Withdrawal amount must be strictly positive."
    
    # if amount enter by the user is greater than balance in the account then returns error message to the user....
    if amount > account["balance"]:
        return "Insufficient balance!"
    
    # deduct the amount from user's bank account and the call record_transaction function to store the record of the transaction into user's account....
    account["balance"] -= amount
    record_transaction(account, "Withdrawal", amount)
    return f"Successfully withdrew Rs. {amount:.2f}"

# returns the records of the transactions made by the user....
def get_transactions(account):
    return account["transactions"]
