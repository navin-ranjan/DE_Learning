# Python Theory & Tutorial

## Table of Contents
1. [Variables, Data Types & Operators](#1-variables-data-types--operators)
2. [Control Flow](#2-control-flow)
3. [Functions & Lambda](#3-functions--lambda)
4. [Data Structures](#4-data-structures)
5. [String Manipulation](#5-string-manipulation)
6. [File Handling](#6-file-handling)
7. [Object-Oriented Programming](#7-object-oriented-programming)
8. [Exception Handling](#8-exception-handling)
9. [Modules & Packages](#9-modules--packages)
10. [Advanced Concepts](#10-advanced-concepts)

---

## 1. Variables, Data Types & Operators

### 📖 What are Variables, Data Types & Operators?

**Variables** are named containers that store data values in memory. In Python, you don't need to declare variables before using them - just assign a value and Python determines the type automatically.

**Data Types** define what kind of data a variable can hold. Python has built-in types like integers, floats, strings, booleans, lists, tuples, sets, and dictionaries.

**Operators** are special symbols that perform operations on variables and values. They include arithmetic operators (+, -, *, /), comparison operators (==, >, <), logical operators (and, or, not), and more.

**Why is this important for Data Engineering?**
- Variables store data transformations and intermediate results
- Understanding data types helps prevent bugs in ETL pipelines
- Operators are used for filtering, calculations, and data comparisons

### Variables
Variables are containers for storing data values. Python has no command for declaring a variable.

```python
# Variable assignment
name = "John"          # String
age = 25               # Integer
salary = 50000.50      # Float
is_active = True       # Boolean

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0

# Type checking
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
```

### Data Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Integer numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"Hello"` | Text/Strings |
| `bool` | `True/False` | Boolean values |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `set` | `{1, 2, 3}` | Unordered, unique elements |
| `dict` | `{"key": "value"}` | Key-value pairs |

### Type Conversion

```python
# Explicit conversion
x = int("42")          # String to int -> 42
y = float(42)          # Int to float -> 42.0
z = str(42)            # Int to string -> "42"
w = list("hello")      # String to list -> ['h', 'e', 'l', 'l', 'o']

# Implicit conversion
a = 5 + 3.0            # int + float = float (8.0)
```

### Operators

```python
# Arithmetic Operators
a, b = 10, 3
print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333...
print(a // b)   # Floor division: 3
print(a % b)    # Modulus: 1
print(a ** b)   # Exponentiation: 1000

# Comparison Operators
print(a == b)   # Equal: False
print(a != b)   # Not equal: True
print(a > b)    # Greater than: True
print(a < b)    # Less than: False
print(a >= b)   # Greater or equal: True
print(a <= b)   # Less or equal: False

# Logical Operators
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Assignment Operators
x = 10
x += 5          # x = x + 5 -> 15
x -= 3          # x = x - 3 -> 12
x *= 2          # x = x * 2 -> 24
x //= 5         # x = x // 5 -> 4

# Identity Operators (compare memory locations)
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is c)       # True (same object)
print(a is b)       # False (different objects)
print(a is not b)   # True

# Membership Operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)        # True
print("grape" not in fruits)    # True
```

---

## 2. Control Flow

### 📖 What is Control Flow?

**Control Flow** refers to the order in which statements are executed in a program. Python provides several control flow tools that allow you to change the execution path based on conditions or iterate over sequences.

**Types of Control Flow:**
- **Conditional Statements (if-elif-else)**: Execute code blocks based on conditions
- **For Loops**: Iterate over sequences (lists, strings, ranges, etc.)
- **While Loops**: Repeat code as long as a condition is true
- **Loop Control (break, continue, pass)**: Control loop execution

**Why is this important for Data Engineering?**
- Conditional logic for data validation and transformation
- Loops for processing batches of data or files
- Control flow for ETL pipeline decision making
- Filtering and transforming data based on conditions

### If-Else Statements

```python
# Basic if statement
age = 18
if age >= 18:
    print("Adult")

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")

# Nested if
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")

# Short-hand if
a, b = 10, 5
result = "a is greater" if a > b else "b is greater"
```

### For Loop

```python
# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):         # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):     # 0, 2, 4, 6, 8 (step of 2)
    print(i)

# Iterate with index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterate over dictionary
person = {"name": "John", "age": 30, "city": "NYC"}
for key in person:                    # Keys only
    print(key)

for key, value in person.items():     # Key-value pairs
    print(f"{key}: {value}")

for value in person.values():         # Values only
    print(value)

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# Loop with else (executes when loop completes normally)
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

### While Loop

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Count reached 5")

# Infinite loop with break
while True:
    response = input("Enter 'quit' to exit: ")
    if response == 'quit':
        break
```

### Loop Control Statements

```python
# Break - exit loop entirely
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# Continue - skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Prints odd numbers: 1, 3, 5, 7, 9

# Pass - placeholder, does nothing
for i in range(5):
    pass  # TODO: implement later
```

---

## 3. Functions & Lambda

### 📖 What are Functions & Lambda?

**Functions** are reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs more modular and maintainable. Functions can accept inputs (parameters) and return outputs.

**Lambda Functions** are small anonymous functions defined with the `lambda` keyword. They can have any number of arguments but only one expression. They're useful for short, simple operations.

**Key Concepts:**
- `def` keyword defines a named function
- `return` sends a value back to the caller
- `*args` captures variable positional arguments
- `**kwargs` captures variable keyword arguments
- `lambda arguments: expression` creates anonymous functions

**Why is this important for Data Engineering?**
- Create reusable data transformation logic
- Apply custom functions to dataframes (Pandas/PySpark)
- Use lambda with map(), filter(), and sorted() for data processing
- Modularize ETL pipeline code for better maintainability

### Function Basics

```python
# Basic function
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("John")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
```

### Parameters & Arguments

```python
# Default parameters
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("John")              # Hello, John!
greet("John", "Hi")        # Hi, John!

# Keyword arguments
def person_info(name, age, city):
    print(f"{name}, {age} years old, from {city}")

person_info(age=30, city="NYC", name="John")  # Order doesn't matter

# *args - Variable positional arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - Variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="NYC")

# Combining all
def function(pos1, pos2, *args, default="value", **kwargs):
    print(f"Positional: {pos1}, {pos2}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")
```

### Lambda Functions

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Lambda with condition
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))  # True

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]

# map() - apply function to all elements
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter() - filter elements
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sorted() with custom key
students = [("John", 85), ("Jane", 90), ("Bob", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)  # [('Jane', 90), ('John', 85), ('Bob', 78)]

# reduce() - apply function cumulatively
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)
```

### Scope

```python
# Local scope
def my_function():
    x = 10  # Local variable
    print(x)

my_function()
# print(x)  # Error: x is not defined outside function

# Global scope
x = 10  # Global variable

def my_function():
    print(x)  # Can access global variable

my_function()  # 10

# Modifying global variable
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # 20

# Nonlocal scope (nested functions)
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)  # 20

outer()
```

---

## 4. Data Structures

### 📖 What are Data Structures?

**Data Structures** are ways of organizing and storing data in memory so that they can be accessed and modified efficiently. Python provides four built-in data structures:

| Data Structure | Ordered | Mutable | Duplicates | Description |
|----------------|---------|---------|------------|-------------|
| **List** | Yes | Yes | Yes | Ordered collection, like an array |
| **Tuple** | Yes | No | Yes | Immutable ordered collection |
| **Set** | No | Yes | No | Unordered collection of unique items |
| **Dictionary** | Yes* | Yes | Keys: No | Key-value pairs |

**Key Concepts:**
- **Mutable**: Can be changed after creation (add, remove, modify)
- **Immutable**: Cannot be changed after creation
- **Ordered**: Maintains the order of elements
- **Indexable**: Can access elements by position

**Why is this important for Data Engineering?**
- Lists for storing sequences of data records
- Dictionaries for JSON data and configurations
- Sets for removing duplicates and set operations
- Tuples for immutable data (database records, coordinates)

### Lists

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty = []
from_list = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# Accessing elements
print(fruits[0])     # First: "apple"
print(fruits[-1])    # Last: "cherry"
print(fruits[1:3])   # Slice: ["banana", "cherry"]

# Modifying lists
fruits[0] = "orange"        # Change element
fruits.append("mango")      # Add to end
fruits.insert(1, "grape")   # Insert at index
fruits.extend(["kiwi", "pear"])  # Add multiple

# Removing elements
fruits.remove("banana")     # Remove by value
popped = fruits.pop()       # Remove last, returns it
fruits.pop(0)               # Remove by index
del fruits[0]               # Delete by index
fruits.clear()              # Remove all

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()              # Sort in place: [1, 1, 2, 3, 4, 5, 6, 9]
numbers.reverse()           # Reverse in place
numbers.index(5)            # Index of first occurrence
numbers.count(1)            # Count occurrences: 2
numbers.copy()              # Create a shallow copy

# List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
matrix = [[i*j for j in range(3)] for i in range(3)]

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6
```

### Tuples

```python
# Creating tuples
point = (3, 4)
single = (42,)           # Single element tuple (comma required)
empty = ()
from_list = tuple([1, 2, 3])

# Accessing elements
print(point[0])          # 3
print(point[-1])         # 4

# Tuple unpacking
x, y = point
print(x, y)              # 3 4

# Multiple return values
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

# Tuple methods
numbers = (1, 2, 2, 3, 2, 4)
print(numbers.count(2))  # 3
print(numbers.index(3))  # 3

# Named tuples
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])
p = Person("John", 30, "NYC")
print(p.name)            # John
```

### Sets

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
empty_set = set()        # NOT {} (that's an empty dict)
from_list = set([1, 2, 2, 3])  # {1, 2, 3}

# Adding and removing
fruits.add("orange")
fruits.update(["mango", "grape"])  # Add multiple
fruits.remove("banana")   # Raises error if not found
fruits.discard("banana")  # No error if not found
fruits.pop()              # Remove arbitrary element
fruits.clear()            # Remove all

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # Union: {1, 2, 3, 4, 5, 6}
print(a & b)    # Intersection: {3, 4}
print(a - b)    # Difference: {1, 2}
print(a ^ b)    # Symmetric difference: {1, 2, 5, 6}

# Set comprehensions
squares = {x**2 for x in range(10)}
evens = {x for x in range(20) if x % 2 == 0}
```

### Dictionaries

```python
# Creating dictionaries
person = {"name": "John", "age": 30, "city": "NYC"}
empty = {}
from_pairs = dict([("a", 1), ("b", 2)])

# Accessing elements
print(person["name"])          # John
print(person.get("age"))       # 30
print(person.get("job", "N/A")) # N/A (default if not found)

# Modifying dictionaries
person["email"] = "john@email.com"  # Add new
person["age"] = 31                   # Update
person.update({"city": "LA", "job": "Engineer"})  # Update multiple
del person["email"]                  # Delete
removed = person.pop("city")         # Remove and return
person.clear()                       # Remove all

# Dictionary methods
print(person.keys())     # dict_keys(['name', 'age'])
print(person.values())   # dict_values(['John', 30])
print(person.items())    # dict_items([('name', 'John'), ('age', 30)])

# Iterating
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehensions
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Nested dictionaries
users = {
    "user1": {"name": "John", "age": 30},
    "user2": {"name": "Jane", "age": 25}
}
print(users["user1"]["name"])  # John
```

---

## 5. String Manipulation

### 📖 What is String Manipulation?

**Strings** are sequences of characters enclosed in quotes (single `'`, double `"`, or triple `'''`). String manipulation involves modifying, searching, and formatting text data.

**Key Concepts:**
- **Immutable**: Strings cannot be changed after creation (operations create new strings)
- **Indexing**: Access characters by position (`s[0]`, `s[-1]`)
- **Slicing**: Extract substrings (`s[1:4]`, `s[::-1]`)
- **Methods**: Built-in functions for string operations (`upper()`, `split()`, `replace()`)

**Common Operations:**
| Operation | Method | Example |
|-----------|--------|---------|
| Convert case | `upper()`, `lower()` | `"Hello".lower()` → `"hello"` |
| Remove whitespace | `strip()` | `" hi ".strip()` → `"hi"` |
| Split string | `split()` | `"a,b,c".split(",")` → `["a","b","c"]` |
| Join strings | `join()` | `"-".join(["a","b"])` → `"a-b"` |
| Replace | `replace()` | `"hi".replace("i","ello")` → `"hello"` |
| Format | f-strings | `f"Hello {name}"` |

**Why is this important for Data Engineering?**
- Parsing CSV, JSON, and log files
- Data cleaning and transformation
- Extracting patterns from text data
- Formatting output and reports

```python
# Creating strings
s1 = 'Hello'
s2 = "World"
s3 = '''Multi-line
string'''
s4 = f"Formatted: {s1} {s2}"

# String indexing and slicing
text = "Hello, World!"
print(text[0])        # H
print(text[-1])       # !
print(text[0:5])      # Hello
print(text[7:])       # World!
print(text[::-1])     # !dlroW ,olleH (reversed)

# String methods
s = "  Hello, World!  "
print(s.strip())       # Remove whitespace: "Hello, World!"
print(s.lower())       # Lowercase: "  hello, world!  "
print(s.upper())       # Uppercase: "  HELLO, WORLD!  "
print(s.replace("World", "Python"))

# Splitting and joining
sentence = "Hello World Python"
words = sentence.split()        # ['Hello', 'World', 'Python']
joined = "-".join(words)        # Hello-World-Python

csv_line = "a,b,c,d"
items = csv_line.split(",")     # ['a', 'b', 'c', 'd']

# String formatting
name, age = "John", 30

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")
print(f"Next year: {age + 1}")
print(f"Float: {3.14159:.2f}")  # Float: 3.14

# format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# String checks
s = "Hello123"
print(s.startswith("Hello"))   # True
print(s.endswith("123"))        # True
print(s.isalpha())              # False (contains digits)
print(s.isdigit())              # False
print(s.isalnum())              # True
print(s.isupper())              # False
print("hello".islower())        # True

# Finding substrsets
s = "Hello, World!"
print(s.find("World"))      # 7 (index or -1)
print(s.index("World"))     # 7 (index or ValueError)
print(s.count("l"))         # 3

# String constants
import string
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # 0123456789
print(string.punctuation)    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

---

## 6. File Handling

### 📖 What is File Handling?

**File Handling** is the process of creating, reading, updating, and deleting files. Python provides built-in functions and modules to work with different file formats including text files, CSV, JSON, and binary files.

**Key Concepts:**
- **File modes**: `r` (read), `w` (write), `a` (append), `x` (create), `b` (binary), `+` (read/write)
- **Context manager**: Use `with` statement for automatic file closing
- **File paths**: Use `os.path` or `pathlib` for cross-platform compatibility
- **File formats**: Text, CSV, JSON, Pickle, Binary

**Common File Operations:**
| Operation | Mode | Description |
|-----------|------|-------------|
| Read file | `r` | Open for reading (default) |
| Write file | `w` | Create/overwrite file |
| Append | `a` | Add to end of file |
| Create | `x` | Create new file (error if exists) |
| Binary | `b` | Binary mode (images, etc.) |

**Why is this important for Data Engineering?**
- Reading data from CSV, JSON, and text files
- Writing processed data to output files
- Working with configuration files
- Handling log files for ETL processes
- Interacting with data lakes and file systems

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()          # Read entire file
    print(content)

with open("example.txt", "r") as file:
    lines = file.readlines()       # Read all lines as list
    print(lines)

with open("example.txt", "r") as file:
    for line in file:              # Read line by line
        print(line.strip())

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appended line\n")

# File modes:
# "r" - Read (default)
# "w" - Write (overwrites)
# "a" - Append
# "x" - Create (fails if exists)
# "b" - Binary mode
# "t" - Text mode (default)
# "+" - Read and write

# Working with JSON
import json

data = {"name": "John", "age": 30, "skills": ["Python", "SQL"]}

# Write JSON
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# Read JSON
with open("data.json", "r") as file:
    loaded = json.load(file)
    print(loaded)

# JSON string conversion
json_string = json.dumps(data, indent=2)
parsed = json.loads(json_string)

# Working with CSV
import csv

# Write CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["John", 30, "NYC"])
    writer.writerows([["Jane", 25, "LA"], ["Bob", 35, "Chicago"]])

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# CSV with DictReader/DictWriter
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])
```

---

## 7. Object-Oriented Programming

### 📖 What is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around "objects" which are instances of classes. Classes serve as blueprints that define attributes (data) and methods (functions) that objects can have. OOP helps model real-world entities and promotes code reusability, modularity, and maintainability.

**Key Concepts:**
- **Class**: Blueprint for creating objects
- **Object**: Instance of a class with actual values
- **Inheritance**: Mechanism for a class to inherit properties from another class
- **Encapsulation**: Hiding internal details and restricting access to data
- **Polymorphism**: Ability to take multiple forms (different classes can be used interchangeably)

**Why is this important for Data Engineering?**
- Building reusable data processing pipelines
- Creating data models that mirror real-world entities
- Implementing clean, maintainable ETL frameworks
- Working with ORM libraries for database interactions

```python
# Basic class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name}")

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Creating objects
p1 = Person("John", 30)
p1.greet()
print(p1)

# Class variables vs Instance variables
class Counter:
    count = 0  # Class variable (shared)

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count  # Instance variable

c1 = Counter()
c2 = Counter()
print(Counter.count)  # 2

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!

# Multiple inheritance
class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(A, B):  # A takes precedence
    pass

c = C()
c.method()  # A

# Encapsulation (private attributes)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)    # Error: private

# Class methods and static methods
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def utility():
        return "I don't need self or cls"

# Property decorator
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
temp.celsius = 30

# Magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Vector(6, 8)
```

---

## 8. Exception Handling

### 📖 What is Exception Handling?

**Exception Handling** is a mechanism to handle runtime errors gracefully without crashing the program. When an error occurs, Python raises an "exception" which can be caught and handled using try-except blocks. This allows developers to anticipate potential errors and provide fallback logic or meaningful error messages.

**Key Concepts:**
- **Exception**: An error that disrupts normal program flow
- **try block**: Code that might raise an exception
- **except block**: Code that handles the exception
- **else block**: Code that runs if no exception occurs
- **finally block**: Code that always runs regardless of exception
- **raise**: Keyword to manually throw an exception

**Common Exceptions:**
| Exception | Description |
|-----------|-------------|
| `ZeroDivisionError` | Division by zero |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File does not exist |
| `ValueError` | Invalid value type |
| `TypeError` | Operation on incompatible type |

**Why is this important for Data Engineering?**
- Handling missing or corrupted data files
- Graceful handling of database connection failures
- Validating data quality and schema
- Creating robust ETL pipelines that don't crash on errors
- Logging errors for debugging and monitoring

```python
#Basic try-except

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Index out of range")
except TypeError:
    print("Type error occurred")

# Generic exception
try:
    x = int("abc")
except Exception as e:
    print(f"An error occurred: {e}")

# Else and finally
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")  # Runs if no exception
finally:
    print("This always runs")   # Always runs

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(e)

# Custom exceptions
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance={balance}, Requested={amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)

# Context managers for resources
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")

# Assert statements
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)
```

---

## 9. Modules & Packages

### 📖 What are Modules & Packages?

**Modules** are individual Python files (`.py`) that contain reusable code. They help organize code into logical units and enable code sharing across different programs. A module can define functions, classes, and variables that can be imported and used in other Python files.

**Packages** are directories that contain multiple modules and a special `__init__.py` file. They provide a hierarchical structure for organizing related modules. Packages can contain subpackages, creating a tree-like organization of code.

**Key Concepts:**
- **Import**: Loading a module into your program using `import` statement
- **From import**: Importing specific items from a module
- **Alias**: Renaming imported items using `as` keyword
- **Package**: Collection of modules in a directory structure
- **Built-in modules**: Pre-installed modules like `math`, `os`, `datetime`, etc.
- **Third-party packages**: External packages installed via pip (e.g., pandas, numpy)

**Why is this important for Data Engineering?**
- Organizing ETL pipeline code into reusable modules
- Using libraries like pandas, numpy, and pyspark for data processing
- Managing dependencies with virtual environments
- Creating shareable and maintainable data processing utilities

```python
# Importing modules
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.14159...

# Import specific functions
from math import sqrt, pi
print(sqrt(25))       # 5.0

# Import with alias
import math as m
print(m.sqrt(36))     # 6.0

# Import all (not recommended)
from math import *

# Common built-in modules

# os - Operating system interface
import os
print(os.getcwd())              # Current directory
os.listdir(".")                 # List directory
os.path.join("folder", "file.txt")  # Join paths
os.path.exists("file.txt")      # Check if exists

# datetime - Date and time
from datetime import datetime, date, timedelta
now = datetime.now()
print(now.year, now.month, now.day)
today = date.today()
tomorrow = today + timedelta(days=1)

# random - Random numbers
import random
print(random.random())          # 0.0 to 1.0
print(random.randint(1, 10))    # Random int 1-10
print(random.choice([1, 2, 3])) # Random element
random.shuffle([1, 2, 3, 4, 5]) # Shuffle list

# collections - Special containers
from collections import Counter, defaultdict, namedtuple

# Counter
words = ["apple", "banana", "apple", "cherry", "apple"]
word_count = Counter(words)
print(word_count)  # Counter({'apple': 3, 'banana': 1, 'cherry': 1})

# defaultdict
dd = defaultdict(int)
dd["a"] += 1  # No KeyError, default is 0

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)

# Creating your own module
# my_module.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# main.py
# from my_module import greet, PI
# print(greet("World"))
# print(PI)

# __name__ == "__main__" pattern
if __name__ == "__main__":
    print("This runs only when executed directly")
```

---

## 10. Advanced Concepts

### 📖 What are Advanced Concepts?

**Advanced Concepts** in Python cover sophisticated programming techniques that go beyond the basics. These include decorators, generators, context managers, and concurrency mechanisms that help write more efficient, readable, and powerful code.

**Key Concepts:**
- **Decorators**: Functions that modify the behavior of other functions (used for logging, timing, authentication)
- **Generators**: Memory-efficient iterators that produce values on-demand using `yield`
- **Context Managers**: Protocol for managing resources (like file handling) with `with` statement
- **Concurrency**: Handling multiple tasks simultaneously through threading and multiprocessing
- **Comprehensions**: Concise syntax for creating lists, sets, and dictionaries

**Why is this important for Data Engineering?**
- Decorators for logging, retry logic, and performance monitoring
- Generators for processing large datasets efficiently (lazy evaluation)
- Context managers for reliable file and database connections
- Multiprocessing for parallel data processing across multiple cores
- Memory-efficient handling of large files and data streams

```python
# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function
# Hello!
# After function

# Decorator with arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))

# Practical decorator - timing
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Decorator with parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
```
---

### Generators

### 📖 What are Generators?

**Generators** are a type of iterable in Python that generate values on-the-fly rather than storing them all in memory. They use the `yield` keyword to return values one at a time, making them memory-efficient for processing large sequences or infinite streams of data.

**Key Concepts:**
- **yield**: Keyword that pauses the function and returns a value
- **Generator function**: A function that uses yield instead of return
- **Generator expression**: Similar to list comprehension but uses parentheses
- **Lazy evaluation**: Values are generated only when requested
- **next()**: Function to get the next value from a generator

**Why is this important for Data Engineering?**
- Processing large datasets without loading everything into memory
- Reading large files line by line efficiently
- Creating data pipelines that handle streaming data
- Reducing memory usage in ETL processes

```python

# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)  # 5, 4, 3, 2, 1

# Generator expression
squares = (x**2 for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1

# Infinite generator
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

counter = infinite_counter()
print(next(counter))  # 0
print(next(counter))  # 1

# Generator with send
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)          # Initialize
print(acc.send(5)) # 5
print(acc.send(3)) # 8

# yield from
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6]
```

### Context Managers

**Context Managers** are objects that define methods to set up and tear down resources. They work with the `with` statement to ensure proper resource management, such as opening and closing files or database connections. Context managers automatically handle cleanup, even if exceptions occur.

**Key Concepts:**
- `with` statement: Automatically manages resource lifecycle
- `__enter__()`: Method called when entering the context
- `__exit__()`: Method called when exiting the context
- `contextmanager`: Decorator for creating context managers using generator functions
- Resource cleanup: Ensures resources are properly released

```python
# Using with statement
with open("file.txt", "w") as f:
    f.write("Hello")

# Creating context manager with class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with FileManager("file.txt", "w") as f:
    f.write("Hello")

# Creating context manager with decorator
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed: {end-start:.4f} seconds")

with timer():
    # Some operation
    sum(range(1000000))
```

### Multithreading & Multiprocessing

**Multithreading** allows multiple threads (lightweight subprocesses) to run concurrently within a single process. Threads share memory space, making communication between them easy. It's ideal for I/O-bound tasks like network requests or file operations.

**Multiprocessing** allows multiple processes to run in parallel, each with its own memory space. It's ideal for CPU-bound tasks that can benefit from multiple CPU cores, such as data processing and computations.

**Key Concepts:**
- **Thread**: Lightweight execution unit within a process
- **Process**: Independent running instance of a program
- **GIL (Global Interpreter Lock)**: Python mechanism that limits true parallel execution in threads
- **Threading module**: For creating and managing threads
- **Multiprocessing module**: For creating and managing processes
- **Pool**: Collection of worker processes for parallel task execution

**When to use which:**
- **Threading**: I/O-bound tasks (network calls, file operations, API requests)
- **Multiprocessing**: CPU-bound tasks (data processing, computations, analytics)

```python
# Threading
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(0.5)
        print(f"Thread 1: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(0.5)
        print(f"Thread 2: {letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

# Multiprocessing
import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)
    print(results)
```

---

## Quick Reference

### Common Built-in Functions

| Function | Description |
|----------|-------------|
| `len()` | Length of object |
| `type()` | Type of object |
| `str()`, `int()`, `float()` | Type conversion |
| `input()` | User input |
| `print()` | Output |
| `range()` | Sequence of numbers |
| `enumerate()` | Index + value pairs |
| `zip()` | Combine iterables |
| `map()` | Apply function to iterable |
| `filter()` | Filter iterable |
| `sorted()` | Sort iterable |
| `reversed()` | Reverse iterable |
| `sum()`, `min()`, `max()` | Math operations |
| `any()`, `all()` | Boolean checks |
| `isinstance()` | Check type |

### List vs Tuple vs Set vs Dict

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| Ordered | Yes | Yes | No* | No* |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No |
| Indexing | Yes | Yes | No | Keys |
| Speed | Slow | Fast | Fast | Fast |

*Python 3.7+ dicts maintain insertion order

---

**Happy Learning! Remember: Practice makes perfect.**