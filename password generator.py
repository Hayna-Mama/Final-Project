import random
import string

def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage
password_length = 12  # Specify the length of the password
password = generate_password(password_length)
print("Generated Password:", password)
