# Python Tasks 2–54 with Explanations
# Author: (Your Name)
# Description: This file contains solved beginner to intermediate Python tasks with detailed comments.

# 2) Print your name
print("My full name is John Doe")  # Prints your full name to the console.

# 3) Print a favorite quote
print("\\In the end, we only regret the chances we didn’t take..\\") # Prints a quote with quotation marks.

      
# 4) Print multiple lines
print("Roses are red,")  # First line of the poem
print("Violets are blue,")  # Second line of the poem
print("Python is fun!")  # Third line of the poem

# 5) Print a simple math result
print("2 + 3 =", 2 + 3)  # Prints the result of the simple math operation (2 + 3)

# 6) Print a shape with symbols
print("  *  ")  # Prints the top of the triangle
print(" *** ")  # Prints the middle of the triangle
print("*****")  # Prints the base of the triangle, forming a shape

# 7) Convert string to integer
num_str = "42"  # String representation of a number
num_int = int(num_str)  # Converts the string '42' to integer 42
print("Converted:", num_int)  # Prints the integer result

# 8) Add two floats
a = 3.5  # First float number
b = 2.5  # Second float number
print("Sum of floats:", a + b)  # Adds the two float numbers and prints the result

# 9) Concatenate two strings
str1 = "Hello"  # First string
str2 = "World"  # Second string
print(str1 + " " + str2)  # Concatenates the two strings with a space in between and prints them

# 10) Print data types
x = 10           # Integer variable
y = "Hello"      # String variable
z = 3.14         # Float variable
print(type(x))   # Prints the type of variable x (int)
print(type(y))   # Prints the type of variable y (str)
print(type(z))   # Prints the type of variable z (float)

# 11) User input and type conversion
age = int(input("Enter your age: "))  # Takes user input (age) and converts it to an integer
print("Next year you will be", age + 1)  # Adds 1 to the entered age and prints the result

# 12) Ask for your name
name = input("What is your name? ")  # Asks the user for their name
print("Hello,", name + "!")  # Prints a greeting with the entered name

# 13) Ask for age and calculate next year’s age
age = int(input("Enter your age: "))  # Takes user input for age
print("You will be", age + 1, "next year.")  # Calculates the age next year by adding 1 and prints the result

# 14) Simple calculator: addition
num1 = int(input("Enter first number: "))  # Takes the first number from the user as an integer
num2 = int(input("Enter second number: "))  # Takes the second number from the user as an integer
print("Sum is:", num1 + num2)  # Adds the two numbers and prints the sum

# 15) Favorite color
color = input("What is your favorite color? ")  # Takes user input for favorite color
print("Your favorite color is", color + "!")  # Prints the favorite color

# 16) Check if the user is tall enough
height = int(input("Enter your height in cm: "))  # Takes user input for height in centimeters
if height > 150:  # Checks if the height is greater than 150 cm
    print("You are tall enough.")  # Prints this message if height is greater than 150 cm
else:
    print("Sorry, you are not tall enough.")  # Prints this message if height is less than or equal to 150 cm

# 17) Print numbers from 1 to 5 using a for loop
for i in range(1, 6):  # Iterates through numbers from 1 to 5
    print(i)  # Prints the current number in the loop

# 18) Print each letter of a string
word = "Python"  # String variable
for letter in word:  # Iterates through each letter of the string
    print(letter)  # Prints each letter of the string on a new line

# 19) Sum of numbers from 1 to 10 using a for loop
sum_numbers = 0  # Initializes a variable to store the sum
for i in range(1, 11):  # Loops through numbers 1 to 10
    sum_numbers += i  # Adds the current number to sum_numbers
print("Sum of numbers from 1 to 10:", sum_numbers)  # Prints the sum of numbers

# 20) Print a multiplication table (1 to 5)
for i in range(1, 6):  # Loops through numbers from 1 to 5
    print(f"2 x {i} = {2 * i}")  # Prints the multiplication table for number 2

# 21) Print even numbers between 2 and 20
for i in range(2, 21, 2):  # Loops through even numbers between 2 and 20
    print(i)  # Prints each even number

# 22) Print numbers from 1 to 5 using a while loop
i = 1  # Initializes the variable i to 1
while i <= 5:  # Continues as long as i is less than or equal to 5
    print(i)  # Prints the value of i
    i += 1  # Increments i by 1

# 23) Sum of numbers from 1 to 5 using a while loop
sum_numbers = 0  # Initializes sum variable
i = 1  # Initializes the loop variable
while i <= 5:  # Continues while i is less than or equal to 5
    sum_numbers += i  # Adds the current value of i to the sum
    i += 1  # Increments i
print("Sum of numbers from 1 to 5:", sum_numbers)  # Prints the sum

# 24) Count down from 10 to 1 using a while loop
i = 10  # Initializes i to 10
while i >= 1:  # Continues while i is greater than or equal to 1
    print(i)  # Prints the current value of i
    i -= 1  # Decreases i by 1 after each iteration

# 25) Print all odd numbers between 1 and 10 using a while loop
i = 1  # Initializes the loop variable i to 1
while i <= 10:  # Loops while i is less than or equal to 10
    if i % 2 != 0:  # Checks if i is an odd number
        print(i)  # Prints i if it's odd
    i += 1  # Increments i

# 26) Ask for user input until they enter "exit"
user_input = ""  # Initialize an empty string to store the user input
while user_input != "exit":  # The loop continues as long as user_input is not "exit"
    user_input = input("Enter something (type 'exit' to quit): ")  # Takes user input
    if user_input != "exit":  # If input is not "exit"
        print("You entered:", user_input)  # Prints the entered input
print("Exiting...")  # Prints exit message once user enters "exit"


# 27) Print all elements of a list
my_list = ["apple", "banana", "cherry"]  # List of fruits
for item in my_list:  # Loops through each element in the list
    print(item)  # Prints the current element

# 28) Find the length of a list
my_list = ["apple", "banana", "cherry"]  # List of fruits
print("Length of the list:", len(my_list))  # Prints the length of the list using len()

# 29) Access a specific element from the list
my_list = [10, 20, 30, 40, 50]  # List of numbers
print("Second element:", my_list[1])  # Prints the second element of the list (index 1)

# 30) Add an element to the list
my_list = [10, 20, 30]  # Initial list
my_list.append(40)  # Adds the number 40 to the list
print("Updated list:", my_list)  # Prints the updated list

# 31) Remove an element from the list
my_list = [10, 20, 30, 40]  # Initial list
my_list.remove(20)  # Removes the element 20 from the list
print("Updated list:", my_list)  # Prints the updated list

# 32) Create a list of squares using list comprehension
squares = [x**2 for x in range(1, 6)]  # Creates a list of squares from 1 to 5
print("Squares:", squares)  # Prints the list of squares

# 33) Create a list of even numbers
even_numbers = [x for x in range(2, 11, 2)]  # Creates a list of even numbers from 2 to 10
print("Even numbers:", even_numbers)  # Prints the list of even numbers

# 34) Filter odd numbers from a list using list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [x for x in numbers if x % 2 != 0]  # Filters out odd numbers
print("Odd numbers:", odd_numbers)  # Prints the list of odd numbers

# 35) Convert a list of strings to uppercase using list comprehension
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]  # Converts each word to uppercase
print("Uppercase words:", uppercase_words)  # Prints the list of uppercase words

# 36) Create a list of numbers squared if divisible by 2
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]  # Squares numbers divisible by 2
print("Squared even numbers:", squared_even_numbers)  # Prints the squared even numbers

# 37) Function to greet a user
def greet_user(name):
    print(f"Hello, {name}!")  # Greets the user by name

greet_user("Alice")  # Calls the function with "Alice" as the argument

# 38) Function to add two numbers
def add_numbers(a, b):
    return a + b  # Returns the sum of two numbers

print(add_numbers(3, 5))  # Calls the function with 3 and 5 as arguments

# 39) Function to check if a number is even or odd
def check_even_or_odd(num):
    if num % 2 == 0:  # Checks if the number is even
        return "Even"
    else:
        return "Odd"  # Returns "Odd" if the number is odd

print(check_even_or_odd(4))  # Calls the function with 4 as an argument

# 40) Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width  # Calculates the area of the rectangle

print(rectangle_area(5, 3))  # Calls the function with 5 and 3 as arguments

# 41) Function to reverse a string
def reverse_string(s):
    return s[::-1]  # Reverses the string

print(reverse_string("hello"))  # Calls the function with "hello" as an argument

# 42) Create and print a tuple
my_tuple = (10, "apple", 3.14)  # Creates a tuple with 3 elements
print(my_tuple)  # Prints the tuple

# 43) Access an element in a tuple
my_tuple = (10, "apple", 3.14)  # Tuple with 3 elements
print("Second element:", my_tuple[1])  # Prints the second element of the tuple

# 44) Find the length of a tuple
my_tuple = (10, "apple", 3.14)  # Tuple with 3 elements
print("Length of the tuple:", len(my_tuple))  # Prints the length of the tuple

# 45) Concatenate two tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
print("Concatenated tuple:", tuple1 + tuple2)  # Concatenates two tuples and prints the result

# 46) Check if an item exists in a tuple
my_tuple = (1, 2, 3, 4)
if 3 in my_tuple:  # Checks if 3 exists in the tuple
    print("Found")  # Prints "Found" if 3 is in the tuple
else:
    print("Not found")  # Prints "Not found" if 3 is not in the tuple

# 47) Create and print a set
my_set = {1, 2, 3}  # Creates a set with 3 elements
print(my_set)  # Prints the set

# 48) Check if an element is in a set
my_set = {1, 2, 3}
if 2 in my_set:  # Checks if 2 is in the set
    print("Yes")  # Prints "Yes" if 2 is found in the set
else:
    print("No")  # Prints "No" if 2 is not found in the set

# 49) Add an element to a set
my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set
print(my_set)  # Prints the updated set

# 50) Remove an element from a set
my_set = {1, 2, 3, 4}
my_set.remove(2)  # Removes 2 from the set
print(my_set)  # Prints the updated set

# 51) Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union of sets:", set1 | set2)  # Prints the union of two sets using the | operator

# 52) Create and print a dictionary
my_dict = {"name": "John", "age": 25}  # Creates a dictionary with two key-value pairs
print(my_dict)  # Prints the dictionary

# 53) Access a value by key
my_dict = {"name": "John", "age": 25}
print("Name:", my_dict["name"])  # Accesses the value associated with the key "name"

# 54) Add a new key-value pair to a dictionary
my_dict = {"name": "John", "age": 25}
my_dict["address"] = "123 Main St"  # Adds a new key-value pair to the dictionary
print(my_dict)  # Prints the updated dictionary

# 55
name="codewa.rs"

# 56 finaly
def get_char(c):
    return chr(c)
