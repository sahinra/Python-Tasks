def main():
    try:
        q1 = input("What's your name?")
        print(f"Hello {q1}, I am your phone book.")

        q2 = int(input("How old are you?"))
        if q2 < 18:
            print("You are so young! Life is ahead of you!")
        elif 18 < q2 < 40:
            print("That's a nice age!")
        else:
            print("You must be very wise!")
    except ValueError:
        print("That doesn't seem to be an integer.")


if __name__ == "__main__":
    main()
