"""
Lesson 1: Variables, Data Types, and Operators
================================================
Python is dynamically typed — you don't declare types explicitly.
"""

# --- Variables ---
# Just assign a value. No 'int x' or 'var x' needed.
name = "Alice"
age = 30
height = 5.7
is_student = False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# --- Core Data Types ---
# int       -> whole numbers:       42, -7, 0
# float     -> decimal numbers:     3.14, -0.5
# str       -> text:                "hello", 'world'
# bool      -> True or False
# NoneType  -> None (represents "nothing")

print("\n--- Checking types ---")
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>
print(type(None))       # <class 'NoneType'>

# --- Type Conversion ---
x = "100"
y = int(x)        # str -> int
z = float(x)      # str -> float
w = str(age)      # int -> str

print("\n--- Type conversions ---")
print(y, type(y))  # 100 <class 'int'>
print(z, type(z))  # 100.0 <class 'float'>
print(w, type(w))  # 30 <class 'str'>

# --- Arithmetic Operators ---
a, b = 10, 3

print("\n--- Arithmetic ---")
print("a + b =", a + b)   # 13   addition
print("a - b =", a - b)   # 7    subtraction
print("a * b =", a * b)   # 30   multiplication
print("a / b =", a / b)   # 3.33 division (always returns float)
print("a // b =", a // b) # 3    floor division (integer result)
print("a % b =", a % b)   # 1    modulus (remainder)
print("a ** b =", a ** b) # 1000 exponent (10^3)

# --- Comparison Operators ---
print("\n--- Comparisons ---")
print("10 == 10:", 10 == 10)  # True   equal
print("10 != 5:", 10 != 5)    # True   not equal
print("10 > 5:", 10 > 5)      # True   greater than
print("10 < 5:", 10 < 5)      # False  less than
print("10 >= 10:", 10 >= 10)  # True   greater or equal
print("10 <= 5:", 10 <= 5)    # False  less or equal

# --- Logical Operators ---
print("\n--- Logical ---")
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("not True:", not True)              # False

# --- Assignment Shortcuts ---
count = 10
count += 5   # same as count = count + 5 -> 15
count -= 3   # 12
count *= 2   # 24
count //= 5  # 4
print("\nFinal count:", count)

# --- Multiple Assignment ---
x, y, z = 1, 2, 3
print(f"\nx={x}, y={y}, z={z}")

# --- f-strings (formatted string literals, Python 3.6+) ---
print(f"\n{name} is {age} years old and {height} feet tall.")
