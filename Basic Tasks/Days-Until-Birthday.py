# Using the datetime library, ask the user for their birthday and calculate how many days are left until their next birthday.

from datetime import datetime

user_input = input("Enter your birthday in the YYYY-DD-MM format: ")
birth_date = datetime.strptime(user_input, "%Y-%d-%m")
today = datetime.today()

print(today - birth_date)