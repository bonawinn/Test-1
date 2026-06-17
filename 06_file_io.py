"""
Lesson 6: File I/O (Input/Output)
==================================
Reading from and writing to files.
"""

# --- Writing to a file ---
# 'w' mode creates the file or overwrites it
with open("example.txt", "w") as f:
    f.write("Line 1: Hello, file!\n")
    f.write("Line 2: Python is fun.\n")
    f.write("Line 3: Learning file I/O.\n")

print("File written successfully.")

# The 'with' statement automatically closes the file when done.
# This is the recommended way to work with files.

# --- Reading an entire file ---
print("\n--- Read entire file ---")
with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# --- Reading line by line ---
print("--- Read line by line ---")
with open("example.txt", "r") as f:
    for line in f:
        print(f"  > {line.strip()}")  # .strip() removes trailing newline

# --- Reading into a list of lines ---
print("\n--- Read into list ---")
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(f"Number of lines: {len(lines)}")
    print(f"First line: {lines[0].strip()}")

# --- Appending to a file ---
# 'a' mode adds to the end without erasing existing content
with open("example.txt", "a") as f:
    f.write("Line 4: This was appended.\n")

print("--- After appending ---")
with open("example.txt", "r") as f:
    print(f.read())

# --- Checking if a file exists ---
import os

filename = "example.txt"
if os.path.exists(filename):
    print(f"'{filename}' exists, size: {os.path.getsize(filename)} bytes")
else:
    print(f"'{filename}' does not exist")

# --- Working with paths (modern way) ---
from pathlib import Path

p = Path("example.txt")
print(f"\nUsing pathlib:")
print(f"  Exists: {p.exists()}")
print(f"  Name: {p.name}")
print(f"  Suffix: {p.suffix}")
print(f"  Absolute: {p.absolute()}")

# pathlib can also read/write:
# content = p.read_text()
# p.write_text("new content")

# --- Clean up ---
os.remove("example.txt")
print("\nCleaned up example.txt")

# --- User input ---
# Uncomment to try interactively:
# name = input("What is your name? ")
# age = int(input("How old are you? "))  # input() always returns str
# print(f"Hello {name}, you are {age} years old!")
