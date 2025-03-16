# Generate a list of numbers from 1 to 10
numbers_1_to_10 = [n for n in range(1, 11)]

# Generate a list of squares of numbers from 1 to 5
squares_1_to_5 = [n**2 for n in range(1, 6)]

# Create a list of all even numbers between 1 and 20
even_numbers = [n for n in range(1, 21) if n % 2 == 0]

# Generate a list of the first letters of each word in a given list
words = ["apple", "banana", "cherry", "date"]
first_letters = [word[0] for word in words]

# Convert all words in a given list to uppercase
uppercase_words = [word.upper() for word in words]

# Generate a list of numbers from 1 to 50 that are divisible by 3
divisible_by_3 = [n for n in range(1, 51) if n % 3 == 0]

# Extract words with more than 4 letters from a given list
long_words = [word for word in words if len(word) > 4]

# Convert a list of temperature values in Celsius to Fahrenheit
celsius_temperatures = [0, 10, 20, 30, 40]
fahrenheit_temperatures = [(c * 9/5) + 32 for c in celsius_temperatures]

# Find all prime numbers between 1 and 100
prime_numbers = [n for n in range(2, 101) if all(n % d != 0 for d in range(2, int(n**0.5) + 1))]

# Extract all words from a sentence that contain at least one vowel and are longer than 5 characters
sentence = "This is an example sentence containing various words"
vowels = "aeiouAEIOU"
filtered_words = [word for word in sentence.split() if any(v in word for v in vowels) and len(word) > 5]

# Generate a sequence of Fibonacci numbers up to the 20th term
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(18)]
