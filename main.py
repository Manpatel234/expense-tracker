expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)
        print("Expense added!")

    elif choice == "2":
        print("All expenses:", expenses)

    elif choice == "3":
        print("Total:", sum(expenses))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")