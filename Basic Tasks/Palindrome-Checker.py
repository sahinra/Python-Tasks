# Write a program that checks if a given word or phrase is a palindrome
# (reads the same backward as forward, ignoring spaces, punctuation, and capitalization).

def clean_string(s):
    # result = []
    # for char in string:
    #     if char.isalnum():
    #         result.append(char.lower())
    return ''.join(e for e in s if e.isalnum()).lower()


def is_palindrome(string):
    return string == string[::-1]


def main():
    input_str = input("Enter a text: ")

    cleaned_input = clean_string(input_str)

    if is_palindrome(cleaned_input):
        print(f"{input_str} is a palindrome.")
    else:
        print(f"{input_str} is not a palindrome.")


if __name__ == "__main__":
    main()