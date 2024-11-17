# 1. Creating a List
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(f"Original list: {fruits}")

# 2. Adding Elements
fruits.append("orange")  # Adds an item to the end
print(f"List after appending: {fruits}")

fruits.insert(1, "mango")  # Inserts at a specific index
print(f"List after inserting 'mango' at index 1: {fruits}")

# 3. Removing Elements
fruits.remove("banana")  # Removes the first occurrence of an item
print(f"List after removing 'banana': {fruits}")

popped_item = fruits.pop()  # Removes the last item and returns it
print(f"Popped item: {popped_item}")
print(f"List after popping: {fruits}")

# 4. Accessing List Elements
first_fruit = fruits[0]  # Access by index
print(f"First fruit: {first_fruit}")

# 5. List Slicing
sliced_fruits = fruits[1:3]  # Get a slice of the list
print(f"Sliced list (index 1 to 2): {sliced_fruits}")

# 6. List Length
list_length = len(fruits)  # Get the number of elements in the list
print(f"Length of the list: {list_length}")

# 7. List Iteration
print("Iterating over the list:")
for fruit in fruits:
    print(fruit)

# 8. List Comprehension
squared_numbers = [x**2 for x in range(5)]  # List comprehension example
print(f"Squared numbers (list comprehension): {squared_numbers}")

# 9. Checking Membership
if "cherry" in fruits:
    print("Cherry is in the list.")

# 10. List Concatenation
more_fruits = ["pear", "grape"]
all_fruits = fruits + more_fruits  # Concatenate two lists
print(f"Concatenated list: {all_fruits}")

# 11. List Sorting
all_fruits.sort()  # Sort the list in-place
print(f"Sorted list: {all_fruits}")

# 12. List Reversing
all_fruits.reverse()  # Reverse the list in-place
print(f"Reversed list: {all_fruits}")

'''
Key Points:
Appending: append() adds an element to the end of the list.
Inserting: insert() adds an element at a specific index.
Removing: remove() removes an item by value, pop() removes and returns an item by index.
Slicing: Allows accessing a sublist using [start:end].
Iteration: Loop through the list using for.
List Comprehension: Compact way to create lists.
Sorting and Reversing: Modify the list in place with sort() and reverse().

'''