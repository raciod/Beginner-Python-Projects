import random
import string

# Getting password length
number_of_characters = int(input("Type the number of characters in your Password: "))
password = ""

# Define character sets
char_sets = [string.ascii_letters, string.digits, string.punctuation]

# Ensure at least one character from each set
for char_set in char_sets:
    password += random.choice(char_set)
    number_of_characters -= 1

# Getting character set for the remaining characters
while number_of_characters > 0:
    choice = random.choice(char_sets)
    password += random.choice(choice)
    number_of_characters -= 1

# Shuffle the password to mix characters
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(f"The random password is: {password}")
