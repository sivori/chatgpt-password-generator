import string
import secrets

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    num_passwords = int(input("How many passwords would you like to generate? "))

    for _ in range(num_passwords):
        print(f"Generated password: {generate_password(password_length)}")
