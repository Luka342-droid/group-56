# 1) Prompt the user to enter a number and handle invalid input
try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Error: Please enter a valid number.")

# 2) Handle IndexError when accessing a non-existing index in a list
my_list = [1, 2, 3]
try:
    print(my_list[5]) 
except IndexError:
    print("Error: Index out of range.")

# 3) Handle TypeError when trying to add an integer to a string
try:
    result = "Number: " + 5
except TypeError:
    print("Error: Cannot add a string and an integer.")
