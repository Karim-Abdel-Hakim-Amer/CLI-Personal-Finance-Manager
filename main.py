import time 
import json 

def show_menu():
    print("================================")
    print("    PERSONAL FINANCE TRACKER")                         
    print("================================")

    print("1. Add transaction")
    print("2. Delete transaction")
    print("3. View transactions")
    print("4. View total spending")
    print("5. Exit")

def add_transaction(transactions):
    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Invalid, please enter amount larger than 0.")
            return False
    except ValueError:
        print("Invalid input, please enter a number.")
        return False
    
    category = input("Category: ")
    category = category.strip()

    if category == "":
        print("The category cannot be empty, please enter a category.")
        return False
    
    description = input("Description: ")
    description = description.strip()

    if description == "":
        print("The description cannot be empty, please enter a description.")
        return False 

    transaction = {
        "amount": amount, 
        "category": category, 
        "description": description
        }
    transactions.append(transaction)
    return True

def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)

        return transactions

    except FileNotFoundError:
        return []

def delete_transaction(transactions):
    if not transactions:
        print("You have no transactions yet.")
        return False

    try:
        transaction_number = int(input("Enter the transaction number to delete: "))
        if transaction_number <= 0:
            print("Invalid input, please enter a transaction number larger than 0.")
            return False
        if transaction_number > len(transactions):
            print("Invalid input, the transaction doesn't exist, please choose an exisiting transaction.")
            return False
    except ValueError:
        print("Invalid input, please enter a number.")
        return False

    transactions.pop(transaction_number - 1)
    print("Transaction deleted.")
    return True
    

def view_transactions(transactions):
    if not transactions:
        print("You have no transactions yet.")
        return
    
    for index, transaction in enumerate(transactions):
        print(f"Transaction number {index + 1}:")
        print(f"amount: {transaction['amount']}")
        print(f"category: {transaction['category']}")
        print(f"description: {transaction['description']}")
        print()

def get_total_spending(transactions):
    total_spending = 0
    for transaction in transactions:
        total_spending = total_spending + transaction["amount"]

    return total_spending
# -----------------------------------------------------------------------------------------------
all_transactions = load_transactions()

while True:
    show_menu()

    try:
        choice = int(input("Choose your action: "))
    except ValueError:
        print("Invalid, please choose one of the available actions.")
        print()
        time.sleep(2)
        continue

    print()
     
    if choice == 1:
        result = add_transaction(all_transactions)
        if result:
            print("Transaction added.")
            save_transactions(all_transactions)
            print()

        time.sleep(2)

    elif choice == 2:
        result = delete_transaction(all_transactions)
        if result:
            save_transactions(all_transactions)
        time.sleep(2)

    elif choice == 3:
        view_transactions(all_transactions)
        time.sleep(2)

    elif choice == 4:
        total_spending = get_total_spending(all_transactions)
        print(f"Total spending: {total_spending}")
        time.sleep(2)

    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid, please select one of the available options.")
        time.sleep(2)
