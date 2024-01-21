# Design a tool that checks if a given password meets certain criteria: a mix of uppercase, lowercase,
# numbers, symbols, and a minimum length. The program should provide feedback on which criteria the password fails.

import string


def check_password(password, min_length=8):
    feedback = []

    if len(password) < min_length:
        feedback.append("Password should be at least {} characters long.".format(min_length))

    if not any(char.isupper() for char in password):
        feedback.append("Password should contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        feedback.append("Password should contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        feedback.append("Password should contain at least one digit.")

    if not any(char in string.punctuation for char in password):
        feedback.append("Password should contain at least one symbol.")

    return feedback


def main():
    try:
        password = input("Please enter the password: ")
        if len(password) > 0:
            feedback = check_password(password)
            if feedback:
                print("Password does not match the criteria. Feedback:")
                for message in feedback:
                    print("- {}".format(message))
            else:
                print("Password matches the criteria.")
        else:
            print("Invalid input. Please enter a valid password.")
    except ValueError:
        print("Invalid input. Please enter a valid password.")


if __name__ == "__main__":
    main()
