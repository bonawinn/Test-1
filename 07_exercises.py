"""
Lesson 7: Practice Exercises
=============================
Try solving these yourself before looking at the solutions below!

How to use:
  1. Read each exercise description
  2. Write your solution in the "YOUR CODE HERE" section
  3. Run the file:  python 07_exercises.py
  4. Check your output against the expected output
  5. Peek at the solutions at the bottom if you get stuck
"""


# ============================================================
# EXERCISE 1: FizzBuzz
# ============================================================
# Print numbers 1-30. For multiples of 3 print "Fizz",
# for multiples of 5 print "Buzz", for both print "FizzBuzz".
#
# Expected output (first 15):
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz

print("=== Exercise 1: FizzBuzz ===")
# YOUR CODE HERE


# ============================================================
# EXERCISE 2: Reverse a string
# ============================================================
# Write a function that reverses a string WITHOUT using [::-1].
#
# reverse_string("hello") -> "olleh"
# reverse_string("Python") -> "nohtyP"

print("\n=== Exercise 2: Reverse String ===")
# YOUR CODE HERE


# ============================================================
# EXERCISE 3: Count vowels
# ============================================================
# Write a function that counts the vowels (a, e, i, o, u)
# in a string (case-insensitive).
#
# count_vowels("Hello World") -> 3
# count_vowels("Python") -> 1

print("\n=== Exercise 3: Count Vowels ===")
# YOUR CODE HERE


# ============================================================
# EXERCISE 4: Find duplicates
# ============================================================
# Given a list, return a new list containing only the
# elements that appear more than once.
#
# find_duplicates([1, 2, 3, 2, 4, 5, 1]) -> [1, 2]

print("\n=== Exercise 4: Find Duplicates ===")
# YOUR CODE HERE


# ============================================================
# EXERCISE 5: Word frequency
# ============================================================
# Count how many times each word appears in a sentence.
# Return a dictionary. Convert to lowercase first.
#
# word_freq("the cat and the dog and the fish")
# -> {"the": 3, "cat": 1, "and": 2, "dog": 1, "fish": 1}

print("\n=== Exercise 5: Word Frequency ===")
# YOUR CODE HERE


# ============================================================
# EXERCISE 6: Temperature converter
# ============================================================
# Write two functions:
#   celsius_to_fahrenheit(c) -> returns (c * 9/5) + 32
#   fahrenheit_to_celsius(f) -> returns (f - 32) * 5/9
#
# Print a conversion table for 0, 20, 37, 100 degrees Celsius.

print("\n=== Exercise 6: Temperature Converter ===")
# YOUR CODE HERE


# ============================================================
# EXERCISE 7: List comprehension challenges
# ============================================================
# Using list comprehensions, create:
# a) A list of squares of even numbers from 1-20
# b) A list of words longer than 4 characters from a sentence
# c) Flatten [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6]

print("\n=== Exercise 7: List Comprehensions ===")
# YOUR CODE HERE


# ============================================================
# EXERCISE 8: Simple calculator
# ============================================================
# Write a function calculator(a, op, b) that takes two numbers
# and an operator string (+, -, *, /) and returns the result.
# Handle division by zero.
#
# calculator(10, "+", 5) -> 15
# calculator(10, "/", 0) -> "Error: division by zero"

print("\n=== Exercise 8: Calculator ===")
# YOUR CODE HERE


# ############################################################
#                       SOLUTIONS
# (Try solving them yourself first!)
# ############################################################

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# --- Solution 1: FizzBuzz ---
print("\n--- Solution 1: FizzBuzz ---")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# --- Solution 2: Reverse String ---
print("\n--- Solution 2: Reverse String ---")
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("hello"))
print(reverse_string("Python"))

# --- Solution 3: Count Vowels ---
print("\n--- Solution 3: Count Vowels ---")
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

print(f"'Hello World' has {count_vowels('Hello World')} vowels")
print(f"'Python' has {count_vowels('Python')} vowel(s)")

# --- Solution 4: Find Duplicates ---
print("\n--- Solution 4: Find Duplicates ---")
def find_duplicates(lst):
    seen = set()
    dupes = set()
    for item in lst:
        if item in seen:
            dupes.add(item)
        seen.add(item)
    return list(dupes)

print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))

# --- Solution 5: Word Frequency ---
print("\n--- Solution 5: Word Frequency ---")
def word_freq(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_freq("the cat and the dog and the fish"))

# --- Solution 6: Temperature Converter ---
print("\n--- Solution 6: Temperature Converter ---")
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print(f"{'Celsius':>10} | {'Fahrenheit':>12}")
print("-" * 25)
for c in [0, 20, 37, 100]:
    print(f"{c:>10} | {celsius_to_fahrenheit(c):>12.1f}")

# --- Solution 7: List Comprehensions ---
print("\n--- Solution 7: List Comprehensions ---")
a = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"a) Squares of evens: {a}")

sentence = "the quick brown fox jumps over the lazy dog"
b = [w for w in sentence.split() if len(w) > 4]
print(f"b) Long words: {b}")

nested = [[1, 2], [3, 4], [5, 6]]
c = [item for sublist in nested for item in sublist]
print(f"c) Flattened: {c}")

# --- Solution 8: Calculator ---
print("\n--- Solution 8: Calculator ---")
def calculator(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        return f"Unknown operator: {op}"

print(f"10 + 5 = {calculator(10, '+', 5)}")
print(f"10 - 3 = {calculator(10, '-', 3)}")
print(f"4 * 7 = {calculator(4, '*', 7)}")
print(f"15 / 4 = {calculator(15, '/', 4)}")
print(f"10 / 0 = {calculator(10, '/', 0)}")
