"""
Lesson 2: Control Flow — if/elif/else, for loops, while loops
==============================================================
Python uses indentation (4 spaces) instead of braces {} to define blocks.
"""

# --- if / elif / else ---
temperature = 72

if temperature > 90:
    print("It's hot outside!")
elif temperature > 70:
    print("It's a nice day.")
elif temperature > 50:
    print("It's a bit cool.")
else:
    print("It's cold!")

# Conditions can be combined with and, or, not
age = 25
has_id = True

if age >= 21 and has_id:
    print("Entry allowed.")

# --- Ternary (inline if) ---
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# --- for loops ---
# Iterate over any sequence (list, string, range, etc.)

print("\n--- for loop with range ---")
for i in range(5):          # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

print("\n--- range(start, stop, step) ---")
for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i, end=" ")
print()

print("\n--- Iterating over a list ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\n--- enumerate: index + value ---")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# --- while loops ---
print("\n--- while loop ---")
countdown = 5
while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1
print("Liftoff!")

# --- break and continue ---
print("\n--- break: exit the loop early ---")
for num in range(10):
    if num == 5:
        break
    print(num, end=" ")
print()  # Output: 0 1 2 3 4

print("\n--- continue: skip to next iteration ---")
for num in range(10):
    if num % 2 == 0:
        continue  # skip even numbers
    print(num, end=" ")
print()  # Output: 1 3 5 7 9

# --- Nested loops ---
print("\n--- Multiplication table (1-3) ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# --- for/else (runs if loop completes without break) ---
print("\n--- for/else ---")
numbers = [2, 4, 6, 8]
for n in numbers:
    if n % 2 != 0:
        print("Found an odd number!")
        break
else:
    print("All numbers were even.")
