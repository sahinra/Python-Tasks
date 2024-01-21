# Convert temperatures from Celsius to Fahrenheit and vice versa.

# easiest solution
print(eval(input("What would you like to calculate?")))

# another solution


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


conversion_type = input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ")

user_input = input("Enter temperature value: ")
temperature = float(user_input)

if conversion_type.upper() == 'C':
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature} Celsius is equal to {result} Fahrenheit")
elif conversion_type.upper() == 'F':
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature} Fahrenheit is equal to {result} Celsius")
else:
    print("Invalid input.")