# Using the random library, generate a random number between 1 and 100 and let the user guess it. Provide feedback on whether the guess is too high, too low, or correct.

import random


def main():
    correct_num = random.randint(1, 100)
    guess = 0

    while guess != correct_num:
        try:
            guess = int(input("Guess a number - "))
            if guess > correct_num:
                print("Too high")
            if guess < correct_num:
                print("Too low")
            if guess == correct_num:
                print("Correct")
                break
        except ValueError:
            print("invalid input")

    print(f"Correct number is {correct_num}")


if __name__ == "__main__":
    main()