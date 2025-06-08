# HackerRank Python Solutions

# 1. Py-If-Else Task
# Uses conditional statements to make decisions based on input values
n = int(input())
if n % 2 == 1:  # Odd number
    print("Weird")
elif 2 <= n <= 5:  # Even and between 2-5
    print("Not Weird")
elif 6 <= n <= 20:  # Even and between 6-20
    print("Weird")
else:  # Even and greater than 20
    print("Not Weird")

print("=" * 50)

# 2. Python Arithmetic Operators
# Performs basic mathematical operations
a = int(input())
b = int(input())
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication

print("=" * 50)

# 3. Compress the String
# Compresses a string by counting consecutive characters
from itertools import groupby

s = input()
result = []
for char, group in groupby(s):
    count = len(list(group))
    result.append(f"({count}, {int(char)})")
print(" ".join(result))

print("=" * 50)

# 4. The Minion Game
# String game where players earn points by forming substrings
def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0  # Vowels
    stuart_score = 0  # Consonants
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

# Example usage:
# minion_game("BANANA")

print("=" * 50)

# 5. Write a Function
# Defines reusable blocks of code using def keyword
def is_leap(year):
    """
    Check if a year is a leap year
    Leap year rules:
    - Divisible by 4 AND (not divisible by 100 OR divisible by 400)
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Example usage:
# year = int(input())
# print(is_leap(year))

print("=" * 50)

# 6. Word Order
# Counts and displays word occurrences while preserving input order
from collections import OrderedDict

n = int(input())
word_count = OrderedDict()

for _ in range(n):
    word = input().strip()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(len(word_count))
print(" ".join(map(str, word_count.values())))

print("=" * 50)

# 7. Iterables and Iterators
# Works with iterators and combinations for sequences and probabilities
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

# Generate all combinations of k letters
all_combinations = list(combinations(letters, k))

# Count combinations containing at least one 'a'
combinations_with_a = [combo for combo in all_combinations if 'a' in combo]

# Calculate probability
probability = len(combinations_with_a) / len(all_combinations)
print(f"{probability:.10f}")

print("=" * 50)

# 8. Python Tuples
# Introduces immutable sequences and hashing
n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))

print("=" * 50)

# 9. Finding the Percentage
# Calculates and formats average marks of a student
n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
average = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")

print("=" * 50)

# 10. Python String Formatting
# Demonstrates string formatting and alignment
def print_formatted(number):
    # Calculate width based on binary representation of the largest number
    width = len(bin(number)[2:])  # Remove '0b' prefix
    
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]  # Remove '0o' prefix
        hexadecimal = hex(i)[2:].upper()  # Remove '0x' prefix and uppercase
        binary = bin(i)[2:]  # Remove '0b' prefix
        
        # Right-align each representation
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

# Example usage:
# n = int(input())
# print_formatted(n)

print("=" * 50)

# Additional utility functions for testing
def test_solutions():
    """Test function to demonstrate the solutions"""
    print("Testing solutions...")
    
    # Test minion game
    print("Minion Game with 'BANANA':")
    minion_game("BANANA")
    
    # Test leap year
    print(f"Is 2020 a leap year? {is_leap(2020)}")
    print(f"Is 1900 a leap year? {is_leap(1900)}")
    print(f"Is 2000 a leap year? {is_leap(2000)}")
    
    # Test string formatting
    print("String formatting for number 5:")
    print_formatted(5)


test_solutions()