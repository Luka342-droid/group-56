from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code or not entered_code:
        return False
    fmt = "%B %d, %Y"   # Example: "July 9, 2015"
    current = datetime.strptime(current_date, fmt)
    expiration = datetime.strptime(expiration_date, fmt)
    return current <= expiration

def in_asc_order(arr):
    return arr == sorted(arr)

def flatten_and_sort(array):
    return sorted([num for sub in array for num in sub])

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    max_a1 = max(len(s) for s in a1)
    min_a1 = min(len(s) for s in a1)
    max_a2 = max(len(s) for s in a2)
    min_a2 = min(len(s) for s in a2)
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))
