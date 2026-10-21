import random

letters = "abcdefghijklmnopqrstuvwxyz"
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*"

all_characters = letters + capitals + numbers + symbols

print("Welcome to the Password Generator!")

while True:
    length = int(input("How long should the password be? (type 0 to quit): "))

    if length == 0:
        print("Bye!")
        break

    if length < 4:
        print("Too short. Please choose 4 or more.")
        continue

    password = ""

    for i in range(length):
        password = password + random.choice(all_characters)

    print("Your password is:", password)
    print()
