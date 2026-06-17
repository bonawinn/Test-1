"""
Lesson 3: Functions and Scope
==============================
Functions let you organize reusable blocks of code.
"""

# --- Basic function ---
def greet(name):
    """Greet someone by name."""
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# --- Return values ---
def add(a, b):
    return a + b

result = add(3, 5)
print(f"\n3 + 5 = {result}")

# --- Default parameters ---
def power(base, exponent=2):
    return base ** exponent

print(f"\n5 squared = {power(5)}")
print(f"2 cubed = {power(2, 3)}")

# --- Keyword arguments ---
def describe_pet(name, animal="dog"):
    print(f"{name} is a {animal}.")

describe_pet("Rex")
describe_pet("Whiskers", animal="cat")
describe_pet(animal="parrot", name="Polly")  # order doesn't matter with keywords

# --- Multiple return values (returns a tuple) ---
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([4, 1, 7, 2, 9])
print(f"\nMin: {lo}, Max: {hi}")

# --- *args: variable number of positional arguments ---
def total(*numbers):
    return sum(numbers)

print(f"\ntotal(1,2,3) = {total(1, 2, 3)}")
print(f"total(10,20) = {total(10, 20)}")

# --- **kwargs: variable number of keyword arguments ---
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nUser info:")
print_info(name="Alice", age=30, city="NYC")

# --- Lambda (anonymous) functions ---
# Small one-line functions, often used with map/filter/sorted.
square = lambda x: x ** 2
print(f"\nLambda square(6) = {square(6)}")

numbers = [3, 1, 4, 1, 5, 9]
sorted_nums = sorted(numbers, key=lambda x: -x)  # sort descending
print(f"Sorted descending: {sorted_nums}")

# --- Scope ---
# Variables inside a function are local. Variables outside are global.
message = "I am global"

def show_scope():
    message = "I am local"  # this is a NEW local variable
    print(message)

show_scope()      # "I am local"
print(message)    # "I am global" — unchanged

# To modify a global variable inside a function, use 'global' (use sparingly):
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(f"\nGlobal counter: {counter}")  # 2

# --- Docstrings ---
def fibonacci(n):
    """
    Return the first n Fibonacci numbers.

    Args:
        n: How many numbers to generate.

    Returns:
        A list of Fibonacci numbers.
    """
    fibs = []
    a, b = 0, 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs

print(f"\nFirst 10 Fibonacci numbers: {fibonacci(10)}")
print(f"Docstring: {fibonacci.__doc__[:40]}...")
