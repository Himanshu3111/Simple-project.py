tasks = []

print("Welcome to your To-Do List!")

while True:
    print()
    print("1. Add a task")
    print("2. See all tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Choose a number: ")

    if choice == "1":
        task = input("Type your task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            number = 1
            for task in tasks:
                print(number, ".", task)
                number = number + 1

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            num = int(input("Which task number to remove? "))
            if num >= 1 and num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Removed:", removed)
            else:
                print("Wrong number.")

    elif choice == "4":
        print("Bye! Do your tasks!")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")
