# Design a program that acts as a simple logbook or journal. Users can add short log entries
# (e.g., "Completed Chapter 5", "Attended Python Workshop") that are written into a log file.
# Display all log entries with timestamps. (Requires: built-in open function)

from datetime import datetime


def create_log_entry(log):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} - {log}\n"


def write_to_log_file(log_file, log_entry):
    with open(log_file, "a") as file:
        file.write(log_entry)
    print("Log entry added successfully.")


def display_all_logs(log_file):
    try:
        with open(log_file, "r") as file:
            log_entries = file.readlines()
            if log_entries:
                print("Log Entries:")
                for entry in log_entries:
                    print(entry, end='')
            else:
                print("No log entries found.")
    except FileNotFoundError:
        print("Log file not found. No entries to display.")


def display_menu():
    print("Logbook")
    print("1. Add a log")
    print("2. Display all logs")
    print("3. Exit")

    try:
        option = int(input("Choose an option: "))
        return option
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return -1


def main():
    LOG_FILE = "logbook.txt"

    option = display_menu()

    while option != 3:
        if option == 1:
            log = input("Write a log: ")
            if log:
                log_entry = create_log_entry(log)
                write_to_log_file(LOG_FILE, log_entry)
            else:
                print("Invalid log entry. Please enter a non-empty log.")
        elif option == 2:
            display_all_logs(LOG_FILE)
        elif option != -1:
            print("Invalid option")
        option = display_menu()

    print("Exiting the program. Goodbye!")


if __name__ == "__main__":
    main()
