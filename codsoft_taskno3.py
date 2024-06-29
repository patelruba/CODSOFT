#Task 3 password generator codsoft 
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired length for the password: "))
    print("Generated Password:", generate_password(length))

