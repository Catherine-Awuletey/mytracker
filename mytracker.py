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

categories = [
    "Inventory",
    "Transportation",
    "Food",
    "Utilities",
    "Entertainment"
]

# adding an expense
def add_expense():
    # ask the user for their description
    description = input("Enter expense description: ")

    print("Choose a category:")
    # print choose a category and print the list of categories
    for index, category in enumerate(categories):
        print(f"{index + 1}. {category}")

    # ask the user to choose a category and run till one is selected
    while True:
        try:
            category_choice = int(input("Enter category number: "))

            # if the enters category is valid, its index is index-1 in our list

            if 1 <= category_choice <= len(categories):
                category = categories[category_choice - 1]
                break
            else:
                # any number outside of our list is invalid
                print("Invalid category number. Please choose a number from the menu.")
                # print if value error
        except ValueError:
            print("Invalid input. Please enter a number." )
                

# ask the user for the amount and run till a valid number is entered
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
    print()

    # add new expense to expenses

    expenses.append(new_expense)

    # call to save expenses in csv file 
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


def expense_summary():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total expenses: {total:.2f}")

    category_totals = {}

    for category in categories:
        category_totals[category] = 0

    for expense in expenses:
        category = expense["category"]
        category_totals[category] += expense["amount"]

    for category, total in category_totals.items():
        print(f"Total expenses for {category}: {total:.2f}")

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
expense_summary()
print("=========================")

