"""
Lesson 5: String Manipulation
==============================
Strings in Python are immutable sequences of characters.
"""

# --- Creating strings ---
single = 'Hello'
double = "World"
multi = """This is
a multi-line
string."""

print(single, double)
print(multi)

# --- Common string methods ---
text = "  Hello, World!  "

print("\n--- String methods ---")
print(f"strip():      '{text.strip()}'")       # remove whitespace
print(f"lower():      '{text.strip().lower()}'")
print(f"upper():      '{text.strip().upper()}'")
print(f"title():      '{'hello world'.title()}'")
print(f"replace():    '{text.strip().replace('World', 'Python')}'")
print(f"startswith(): {text.strip().startswith('Hello')}")
print(f"endswith():   {text.strip().endswith('!')}")

# --- Splitting and joining ---
csv_line = "apple,banana,cherry,date"
fruits = csv_line.split(",")
print(f"\nSplit: {fruits}")

rejoined = " | ".join(fruits)
print(f"Joined: {rejoined}")

# Split by whitespace (default)
sentence = "Python is great"
words = sentence.split()
print(f"Words: {words}")

# --- String indexing and slicing ---
s = "Python"
print(f"\n--- Indexing ---")
print(f"s[0] = '{s[0]}'")    # P
print(f"s[-1] = '{s[-1]}'")  # n
print(f"s[0:3] = '{s[0:3]}'")  # Pyt
print(f"s[::-1] = '{s[::-1]}'")  # nohtyP (reversed)

# --- Searching ---
text = "The quick brown fox jumps over the lazy dog"
print(f"\n--- Searching ---")
print(f"find('fox'):   {text.find('fox')}")       # 16 (index)
print(f"find('cat'):   {text.find('cat')}")       # -1 (not found)
print(f"count('the'):  {text.count('the')}")      # 1 (case-sensitive)
print(f"'fox' in text: {'fox' in text}")           # True

# --- Formatting ---
name = "Alice"
age = 30
score = 95.678

print("\n--- Formatting ---")
# f-strings (recommended, Python 3.6+)
print(f"{name} is {age} years old.")
print(f"Score: {score:.2f}")           # 2 decimal places
print(f"{'centered':^20}")             # center in 20 chars
print(f"{'left':<20}|")               # left-align
print(f"{'right':>20}")               # right-align
print(f"Binary of 42: {42:b}")        # 101010
print(f"Hex of 255: {255:x}")         # ff
print(f"With commas: {1000000:,}")    # 1,000,000

# .format() method (older style, still useful)
print("\nHello, {}! You are {} years old.".format(name, age))

# --- Useful checks ---
print("\n--- Character checks ---")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")   # True
print(f"'abc'.isalpha():    {'abc'.isalpha()}")       # True
print(f"'123'.isdigit():    {'123'.isdigit()}")       # True
print(f"'  '.isspace():     {'  '.isspace()}")        # True

# --- Escape characters ---
print("\n--- Escape characters ---")
print("Tab:\tHere")
print("Newline:\nHere")
print("Backslash: \\")
print("Quote: \"hello\"")

# Raw strings (ignore escapes, useful for regex and file paths)
path = r"C:\Users\name\Documents"
print(f"Raw string: {path}")
