# Importing NumPy for advanced indexing examples
import numpy as np

# 1. List Indexing
print("1. List Indexing")
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Numerical indexing
print("Element at index 2:", my_list[2])  # 30

# Slicing
print("Slice [1:4]:", my_list[1:4])  # [20, 30, 40]

# Negative indexing
print("Last element (Negative Index):", my_list[-1])  # 50

# Step slicing
print("Every second element:", my_list[::2])  # [10, 30, 50]

print("\n")

# 2. Tuple Indexing
print("2. Tuple Indexing")
my_tuple = (100, 200, 300, 400, 500)
print("Original Tuple:", my_tuple)

# Numerical indexing
print("Element at index 3:", my_tuple[3])  # 400

# Slicing
print("Slice [1:4]:", my_tuple[1:4])  # (200, 300, 400)

# Negative indexing
print("First element (Negative Index):", my_tuple[-5])  # 100

print("\n")

# 3. String Indexing
print("3. String Indexing")
my_string = "Hello, World!"
print("Original String:", my_string)

# Numerical indexing
print("Character at index 7:", my_string[7])  # W

# Slicing
print("Substring [0:5]:", my_string[0:5])  # Hello

# Negative indexing
print("Last character (Negative Index):", my_string[-1])  # !

# Step slicing
print("Every second character:", my_string[::2])  # Hlo ol!

print("\n")

# 4. NumPy Array Indexing
print("4. NumPy Array Indexing")
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:\n", my_array)

# Numerical indexing
print("Element at row 1, col 2:", my_array[1, 2])  # 6

# Slicing rows and columns
print("First two rows and cols:\n", my_array[:2, :2])  # [[1, 2], [4, 5]]

# Negative indexing
print("Last row:", my_array[-1])  # [7, 8, 9]

# Boolean indexing
print("Elements > 5:", my_array[my_array > 5])  # [6, 7, 8, 9]

# Fancy indexing
print("Select specific rows and cols:\n", my_array[[0, 2], [1, 2]])  # [2, 9]

print("\n")
