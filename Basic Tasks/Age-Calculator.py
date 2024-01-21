# Ask the user for their birth year and calculate their age.
import datetime

current_year = int(datetime.date.today().year)
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"Your age is:{age}")
