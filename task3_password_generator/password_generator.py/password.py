import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

# Get password length from the user
length = int(input("Enter the desired password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("\nGenerated Password:")
print(password)