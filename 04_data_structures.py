"""
Lesson 4: Data Structures — Lists, Tuples, Dictionaries, Sets
==============================================================
These are the four built-in collection types you'll use constantly.
"""

# ============================================================
# LISTS — ordered, mutable, allows duplicates
# ============================================================
print("=== LISTS ===")
colors = ["red", "green", "blue"]

# Accessing elements (0-indexed)
print(colors[0])    # "red"
print(colors[-1])   # "blue" (last element)

# Slicing [start:stop:step]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])    # [2, 3, 4]
print(nums[:3])     # [0, 1, 2]
print(nums[7:])     # [7, 8, 9]
print(nums[::2])    # [0, 2, 4, 6, 8]  every 2nd element
print(nums[::-1])   # [9, 8, 7, ...] reversed

# Modifying
colors.append("yellow")         # add to end
colors.insert(1, "orange")      # insert at index 1
colors.extend(["purple", "pink"])  # add multiple items
print(colors)

removed = colors.pop()          # remove & return last
colors.remove("orange")         # remove first occurrence
print(f"Removed: {removed}, List: {colors}")

# Useful methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nLength: {len(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

numbers.sort()
print(f"Sorted: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

# List comprehensions — powerful and Pythonic!
squares = [x**2 for x in range(10)]
print(f"\nSquares: {squares}")

evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# ============================================================
# TUPLES — ordered, immutable, allows duplicates
# ============================================================
print("\n=== TUPLES ===")
point = (3, 4)
rgb = (255, 128, 0)

# Access like lists
print(f"x={point[0]}, y={point[1]}")

# Unpacking
x, y = point
r, g, b = rgb
print(f"RGB: r={r}, g={g}, b={b}")

# Tuples are immutable — you CANNOT modify them:
# point[0] = 10  # This would raise TypeError

# Single-element tuple needs a trailing comma
single = (42,)
not_a_tuple = (42)   # this is just an int!
print(f"Tuple: {type(single)}, Not tuple: {type(not_a_tuple)}")

# ============================================================
# DICTIONARIES — key:value pairs, ordered (Python 3.7+), mutable
# ============================================================
print("\n=== DICTIONARIES ===")
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access values
print(person["name"])
print(person.get("phone", "N/A"))  # .get() with default, avoids KeyError

# Modify
person["age"] = 31             # update existing
person["email"] = "a@b.com"   # add new key
del person["city"]             # delete key
print(person)

# Looping through dictionaries
print("\nKeys and values:")
for key, value in person.items():
    print(f"  {key} -> {value}")

print("\nJust keys:", list(person.keys()))
print("Just values:", list(person.values()))

# Check membership
print(f"Has 'name'? {'name' in person}")

# Dictionary comprehension
word = "mississippi"
letter_count = {ch: word.count(ch) for ch in set(word)}
print(f"\nLetter counts in '{word}': {letter_count}")

# ============================================================
# SETS — unordered, mutable, NO duplicates
# ============================================================
print("\n=== SETS ===")
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate ignored
print(f"Fruits: {fruits}")  # only 3 items

# Add/remove
fruits.add("date")
fruits.discard("banana")  # remove (no error if missing)
print(f"Updated: {fruits}")

# Set operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"\nUnion:        {a | b}")        # all elements
print(f"Intersection: {a & b}")          # common elements
print(f"Difference:   {a - b}")          # in a but not b
print(f"Symmetric:    {a ^ b}")          # in one but not both

# Great for removing duplicates
dupes = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(dupes))
print(f"\nDeduplicated: {unique}")

# ============================================================
# WHEN TO USE WHAT
# ============================================================
print("\n=== Quick Guide ===")
print("List  -> ordered collection, need to modify items")
print("Tuple -> ordered collection, data shouldn't change")
print("Dict  -> map keys to values, fast lookups by key")
print("Set   -> unique items, fast membership testing, set math")
