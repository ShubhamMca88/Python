# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding elements to a set
fruits.add("orange")
print(f"Updated fruits set: {fruits}")

# Removing an element from the set
fruits.remove("banana")
print(f"Fruits set after removal: {fruits}")

# Set operations: Union, Intersection, Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1 | set2
print(f"Union: {union_set}")

# Intersection
intersection_set = set1 & set2
print(f"Intersection: {intersection_set}")

# Difference
difference_set = set1 - set2
print(f"Difference: {difference_set}")

# Checking membership
if "apple" in fruits:
    print("Apple is in the fruits set.")

# Set comprehension
squares = {x**2 for x in range(5)}
print(f"Set comprehension (squares): {squares}")

'''
Key Points:
Set: A collection of unique elements.
Adding: Use .add() to add elements.
Removing: Use .remove() to remove elements.
Set Operations: Union (|), Intersection (&), Difference (-).
Membership: Use in to check if an element exists in a set.
Set Comprehension: Like list comprehension, but for sets. 

'''