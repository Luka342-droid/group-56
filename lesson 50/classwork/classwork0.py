# 1
def safe_divide(a, b):
    try:
        return a / b
    except TypeError:
        return "Error: Invalid input type!"
# 2 
def check_number(value):
    try:
        num = float(value) 
        return f"Valid number: {num}"
    except ValueError:
        return "Error: Input is not a valid number!"
