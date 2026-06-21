import random
import string

print("=" * 40)
print("      Password Generator")
print("=" * 40)

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
        exit()

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    print("\nGenerated Password: " )
    print(password)
except ValueError:
    print("Please enter a valid number.")