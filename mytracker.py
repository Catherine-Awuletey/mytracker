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
        print("Feature coming soon")
        print()
    elif choice == "2":
        print("Feature coming soon")
        print()
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid option. Please try again.")
        print()
print("Goodbye!")
print("=========================")