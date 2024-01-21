# Accept a list of numbers from the user and print the sorted list.

user_input = input("Enter a list of numbers separated by spaces: ")
list_numbers = []

for num in user_input.split(','):
    list_numbers.append(int(num))

list_numbers.sort()
print("Sorted List:", list_numbers)
