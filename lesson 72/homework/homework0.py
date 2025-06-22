# You're a square!
def is_square(n):
    if n < 0: return False

    #if int(n0.5)int(n0.5)==n: return True
    return False
# Get the Middle Character
def get_middle(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]
# Isograms
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))
# Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")
# Jaden Casing Strings
def to_jaden_case(string):
    string = [i.capitalize() for i in string.split(" ")]
    return " ".join(string)

# საკლასო დავალება:

# შეასრულეთ ამოცანა:

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(st):
    result = ""
    for i, char in enumerate(st):
        part = char.upper() + char.lower() * i
        if i > 0:
            result += "-" + part
        else:
            result += part
    return result

#Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]
# Complementary DNA
def DNA_strand(dna):
    res = ""

    for base in dna:
        if base == "A": res+="T"
        elif base == "T": res+="A"
        elif base == "C": res+="G"
        else: res+="C"

# Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    return sum(range(min(a, b), max(a,b)+1))

# Friend or Foe?
def friend(x):
    res = []
    for i in x:
        if len(i) == 4:
            res.append(i)
    return res

# Credit Card Mask
def maskify(cc):
    if len(cc) <= 4:
        return cc
    res = ""
    for i in range(len(cc)):
        if i < len(cc) - 4:
            res+="#"
        else: res+=cc[i]
    return res

# საკლასო დავალება:

# შეასრულეთ ამოცანა:

# https://www.codewars.com/kata/551f37452ff852b7bd000139

def add_binary(a,b):
    return bin(a + b)[2:]

# 2-6)

# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()
# https://www.codewars.com/kata/56606694ec01347ce800001b
def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and \
        a + b > c and a + c > b and b + c > a
