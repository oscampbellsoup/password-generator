# Import random module
import random

# List of letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message; inputs
print("Welcome to the Password Generator!")
amount_letters = int(input("How many letters would you like in your password?\n"))
amount_symbols = int(input("How many symbols would you like?\n"))
amount_numbers = int(input("How many numbers would you like?\n"))

# Creating a list for all the randomly selected characters for the password
password_list = [ ]

# Select random characters according to the inputs
for char in range(0, amount_letters):
    password_list += random.choice(letters)

for char in range (0, amount_numbers):
    password_list += random.choice(numbers)
    
for char in range (0, amount_symbols):
    password_list += random.choice(symbols)

# List of random characters are shuffled
random.shuffle(password_list)

# Password variable created to turn list into a string.
password = ""
for char in password_list:
    password += char
    
# Output message
print(f"Your password is {password}")