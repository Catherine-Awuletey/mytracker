import csv

# welcome
print("=========================")
print()
print("    CHARM ME UP")
print("   Expense Tracker")
print()
print("=========================")
print()
print("Welcome to My Tracker!") 
print()
name = input("Enter your name: ")
print()
print(f"Hello {name}, let's get started!")
print()

expenses = []

def add_expense():
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

    print()

    new_expense = {
        "description": description,
        "category": category,
        "amount": amount
    }   

    print("Expense added successfully!")

    print()

    print(new_expense)

    # print(f"Description: {expense}")
    # print(f"Category: {category}")
    # print(f"Amount: {amount}")

    expenses.append(new_expense)
    save_expenses()
    print("current expenses: ", expenses)

def view_expenses():
    print("Your expenses")
    print()

    for index, expense in enumerate(expenses):
        print(f"{index + 1}. Description: {expense['description']}, Category: {expense['category']}, Amount: {expense['amount']}")

def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Description", "Category", "Amount"])
        for expense in expenses:
            writer.writerow([
                expense["description"],
                  expense["category"],
                    expense["amount"]])   
        
def load_expenses():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                description = row[0]
                category = row[1]
                amount = float(row[2])

                expenses.append({
                    "description": description,
                    "category": category,
                    "amount": amount
                })

    except FileNotFoundError:
        pass

load_expenses()

choice = ""

# while loop to run after each input and exit on 3
while choice != "3":
    # display the menu on each refresh and get input
    print("=========================")
    print("Menu")
    print("=========================")
    print()
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    print()
    print("=========================")
    print()
    choice = input("Enter your option: ")
    print()
    
    if choice == "1":
        add_expense()
        print()
    elif choice == "2":
        view_expenses()
        save_expenses()
        print()
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid option. Please try again.")
        print()
print("Goodbye!")
print("=========================")

load_expenses()

