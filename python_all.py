# 1. Basic Python Syntax
print("Hello, World!")

# 2. Variables and Data Types
x = 10
y = 3.14
name = "Shubham"
is_active = True
print(f"Variables - x: {x}, y: {y}, name: {name}, active: {is_active}")

# 3. Conditional Statements
age = 25
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 4. Loops
print("For Loop:")
for i in range(5):
    print(i)

print("While Loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# 5. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Shubham"))

# 6. Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(f"List of fruits: {fruits}")
print(f"Second fruit: {fruits[1]}")

# 7. Dictionaries
person = {"name": "Shubham", "age": 25, "city": "Delhi"}
print(f"Person's name: {person['name']}")

# 8. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Shubham", 25)
print(person1.greet())

# 9. Exception Handling
try:
    x = 10 / 0  # This will raise an exception
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 10. File Handling
with open("example.txt", "w") as file:
    file.write("Hello, this is a test.")
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File content: {content}")

# 11. List Comprehensions
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# 12. Lambda Functions
square = lambda x: x**2
print(f"Square of 5: {square(5)}")

# 13. Map, Filter, Reduce
from functools import reduce

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

sum_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers: {sum_numbers}")

# 14. Decorators
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# 15. Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("Countdown:")
for i in countdown(5):
    print(i)
