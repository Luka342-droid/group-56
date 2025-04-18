def get_average(marks):
    return sum(marks) // len(marks)

def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"

def reverse_words(s):
    return " ".join(s.split(' ')[::-1])

def cockroach_speed(s):
    return int(s*27.777778)

def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]

def square(n):
    return n*n

def remove_every_other(my_list):
    return my_list[::2]

def is_even(n): 
    return n % 2 == 0

def get_planet_name(id):
    if id == 1: return "Mercury"
    elif id == 2: return "Venus"
    elif id == 3: return "Earth"
    elif id == 4: return "Mars"
    elif id == 5: return "Jupiter"
    elif id == 6: return "Saturn"
    elif id == 7: return "Uranus"
    elif id == 8: return "Neptune"

def enough(cap, on, wait):
    available = cap - on

    if available >= wait: return 0
    return wait - available

def between(a,b):
    return list(range(a, b+1))

def is_uppercase(inp):
    return inp == inp.upper()

