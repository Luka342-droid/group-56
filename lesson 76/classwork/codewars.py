# Sum of odd numbers
def row_sum_odd_numbers(n):
    start = n * n - (n - 1)
    return sum(start + 2 * i for i in range(n))
# Printer Errors
def printer_error(s):
    valid = "abcdefghijklm"
    res = 0

    for i in s:
        if i not in valid: res += 1

    return f"{res}/{len(s)}"
# Reverse words
def reverse_words(text):
    str_list=text.split(" ")
    result = []
    for i in str_list:
        result.append(i[::-1])
    return " ".join(result)
# Ones and Zeros
def binary_array_to_number(arr):
    res = ""
    for bit in arr:
        res += str(bit)
    return int(res, 2)

# საკლასო დავალება:

# შეასრულეთ ამოცანა: 
# https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
    people_in_bus = 0
    for on, off in bus_stops:
        people_in_bus += on - off
    return people_in_bus

# საკლასო დავალება:

# შეასრულეთ ამოცანა:

# https://www.codewars.com/kata/5949481f86420f59480000e7
def odd_or_even(arr):
    total = sum(arr)
    if total % 2 == 0: 
        return "even" 
    else:
        return "odd"

# საკლასო დავალება:

# შეასრულეთ ამოცანა:

# https://www.codewars.com/kata/559590633066759614000063
def min_max(lst):
    return [min(lst), max(lst)]