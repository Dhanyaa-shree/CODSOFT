import random 
import string

def collect_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length:"))
            if length <= 0:
                print("please enter a positive number greater than zero.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ' '.join(random.choice(characters) for _ in range(length))
    return password

def show_password(password):
    print(f"\nyour newly generated password is: {password}")
    
def main():
    print("welcome to the custom password generator!")
    password_length = collect_user_input()
    password = generate_secure_password(password_length)
    show_password(password)

if __name__ == "__main__":
    main()