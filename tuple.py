# 1. Creating a Tuple
fruits = ("apple", "banana", "cherry")
print(f"Original tuple: {fruits}")

# 2. Accessing Tuple Elements
first_fruit = fruits[0]  # Access by index
print(f"First fruit: {first_fruit}")

# 3. Tuple Slicing
sliced_fruits = fruits[1:3]  # Get a slice of the tuple
print(f"Sliced tuple (index 1 to 2): {sliced_fruits}")

# 4. Length of Tuple
tuple_length = len(fruits)  # Get the number of elements in the tuple
print(f"Length of the tuple: {tuple_length}")

# 5. Iterating Over a Tuple
print("Iterating over the tuple:")
for fruit in fruits:
    print(fruit)

# 6. Tuple Concatenation
more_fruits = ("pear", "grape")
all_fruits = fruits + more_fruits  # Concatenate two tuples
print(f"Concatenated tuple: {all_fruits}")

# 7. Tuple Repetition
repeated_fruits = fruits * 2  # Repeat the tuple
print(f"Repeated tuple: {repeated_fruits}")

# 8. Checking Membership
if "banana" in fruits:
    print("Banana is in the tuple.")

# 9. Nested Tuple
nested_tuple = ("apple", ("orange", "pear"))
print(f"Nested tuple: {nested_tuple}")
