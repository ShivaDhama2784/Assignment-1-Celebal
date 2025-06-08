# Celebal Internship – Assignment 1 Solutions

This repository contains Python solutions for Assignment 1 of the Celebal Internship Program. The tasks are aimed at improving fundamental programming concepts including conditionals, string manipulation, loops, functions, data structures, and basic algorithmic logic.

---

## 📝 Contents

Below is the list of problems solved in this assignment along with a brief description:

1. **Py-If-Else**  
   Uses conditional statements to print output based on whether a given number is odd, even, and within certain ranges.

2. **Python Arithmetic Operators**  
   Takes two integers and performs basic arithmetic operations: addition, subtraction, and multiplication.

3. **Compress the String**  
   Utilizes the `groupby` function from `itertools` to compress consecutive characters of a string and count their occurrences.

4. **The Minion Game**  
   A string game where two players (Kevin and Stuart) score points based on substrings starting with vowels or consonants.

5. **Write a Function (`is_leap`)**  
   Determines if a year is a leap year based on divisibility rules (including the century rule).

6. **Word Order**  
   Counts occurrences of words from input while preserving the order of first appearances using `OrderedDict`.

7. **Iterables and Iterators**  
   Calculates the probability that a randomly chosen combination contains a specific character (`'a'`) using `itertools.combinations`.

8. **Python Tuples**  
   Demonstrates the immutability of tuples and computes a hash value for a tuple of integers.

9. **Finding the Percentage**  
   Computes and prints the average marks for a queried student name with proper formatting.

10. **Python String Formatting**  
    Prints numbers from `1` to `n` in decimal, octal, hexadecimal, and binary formats with right alignment.

---

## 🧪 Testing Utilities

A `test_solutions()` utility function is included to demonstrate outputs of selected problems:

```python
# Test minion game
minion_game("BANANA")

# Test leap year
print(is_leap(2020))  # True
print(is_leap(1900))  # False
print(is_leap(2000))  # True

# Test string formatting
print_formatted(5)
