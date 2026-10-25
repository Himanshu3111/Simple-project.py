print("Welcome to the Temperature Converter!")

while True:
    print()
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

    choice = input("Choose a number: ")

    if choice == "1":
        celsius = float(input("Type the temperature in Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(celsius, "C is equal to", fahrenheit, "F")

    elif choice == "2":
        fahrenheit = float(input("Type the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(fahrenheit, "F is equal to", round(celsius, 2), "C")

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Please choose 1, 2, or 3.")
