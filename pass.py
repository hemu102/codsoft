import string
import random

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Define the possible character set for the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password using a combination of random characters
password = ''.join(random.choice(characters) for i in range(password_length))

# Display the generated password on the screen
print("Generated password:", password)