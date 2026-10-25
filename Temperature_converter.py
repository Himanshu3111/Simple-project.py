print("Welcome to the Temperature Converter!")

while True:
    print()
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("0. Quit")

    choice = input("Choose a number: ")

    if choice == "1":
        celsius = float(input("Type the temperature in Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(celsius, "C is equal to", round(fahrenheit, 2), "F")

    elif choice == "2":
        fahrenheit = float(input("Type the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(fahrenheit, "F is equal to", round(celsius, 2), "C")

    elif choice == "3":
        celsius = float(input("Type the temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(celsius, "C is equal to", round(kelvin, 2), "K")

    elif choice == "4":
        kelvin = float(input("Type the temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(kelvin, "K is equal to", round(celsius, 2), "C")

    elif choice == "5":
        fahrenheit = float(input("Type the temperature in Fahrenheit: "))
        kelvin = ((fahrenheit - 32) * 5 / 9) + 273.15
        print(fahrenheit, "F is equal to", round(kelvin, 2), "K")

    elif choice == "6":
        kelvin = float(input("Type the temperature in Kelvin: "))
        fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
        print(kelvin, "C is equal to", round(fahrenheit, 2), "F")

    elif choice == "0":
        print("Bye!")
        break

    else:
        print("Please choose 1, 2, 3, 4, or 5.")
