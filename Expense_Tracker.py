expenses = []

print("Welcome to your Expense Tracker!")

while True:
    print()
    print("1. Add an expense")
    print("2. See all expenses")
    print("3. See total")
    print("4. Quit")

    choice = input("Choose a number: ")

    if choice == "1":
        item = input("What did you buy? ")
        amount = float(input("How much did it cost? "))
        expenses.append((item, amount))
        print("Expense saved!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            for item, amount in expenses:
                print(item, ": Rs", amount)

    elif choice == "3":
        total = 0
        for item, amount in expenses:
            total = total + amount
        print("You spent Rs", total, "in total.")

    elif choice == "4":
        print("Bye! Save your money!")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")
