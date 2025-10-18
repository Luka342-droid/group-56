def show_sequence(n):
    if n < 0:
        return f"{n}<0"
    if n == 0:
        return "0=0"
    return "+".join(str(i) for i in range(n+1)) + f" = {sum(range(n+1))}"

def vowel_indices(word):
    vowels = 'aeiouy'
    indices = []
    for i, c in enumerate(word.lower()):
        if c in vowels:
            indices.append(i + 1)
    return indices

def largest_pair_sum(numbers):
    # Find the largest and second largest numbers
    first = second = float('-inf')

    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num

    return first + second
