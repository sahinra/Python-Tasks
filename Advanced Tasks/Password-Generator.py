# Create a program that generates strong passwords with a mix of uppercase, lowercase, numbers, and
# symbols. Allow users to specify the length.
import random
import string


def create_password(length):
    if length < 5:
        raise ValueError("Password length should be at least 5.")
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = string.punctuation

    all_chars = uppercase_chars + lowercase_chars + digit_chars + symbol_chars
    shuffled_chars = random.sample(all_chars, k=len(all_chars))

    return ''.join(shuffled_chars[:length])


def main():
    try:
        length = int(input("Please enter the length of the password (at least 5): "))
        password = create_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid length.")


if __name__ == "__main__":
    main()
