# Python Practice Exercises
# =========================
# Instructions:
# 1. Complete the exercises for the current topic you're studying
# 2. Write your solutions in the designated areas
# 3. Test your code by running this file
# 4. When done, CLEAR your solutions and move to the next topic
# =========================


# =============================================================================
# TOPIC 1: Variables, Data Types & Operators
# =============================================================================

# Exercise 1.1: Create variables of each type and print their types
# TODO: Create a string, integer, float, boolean, list, tuple, set, and dictionary
# YOUR CODE HERE:
s = 'this is my code'
print(s)
print(type(s))


# Exercise 1.2: Type conversion
# Convert the string "42" to integer, then to float
# YOUR CODE HERE:



# Exercise 1.3: Arithmetic operators
# Calculate: (10 + 5) * 2 / 5 - 3
# YOUR CODE HERE:



# Exercise 1.4: Comparison and logical operators
# Check if 10 is greater than 5 AND 20 is less than 30
# YOUR CODE HERE:



# Exercise 1.5: Membership operators
# Check if "apple" is in the list ["banana", "apple", "cherry"]
# YOUR CODE HERE:



# =============================================================================
# TOPIC 2: Control Flow
# =============================================================================

# Exercise 2.1: Write an if-elif-else to grade scores
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F
# YOUR CODE HERE:
score = 85
# Print the grade



# Exercise 2.2: For loop - Print numbers 1 to 10
# YOUR CODE HERE:



# Exercise 2.3: For loop with enumerate - Print index and value
fruits = ["apple", "banana", "cherry"]
# YOUR CODE HERE:



# Exercise 2.4: While loop - Print even numbers from 2 to 20
# YOUR CODE HERE:



# Exercise 2.5: Nested loops - Print multiplication table (1-5)
# YOUR CODE HERE:



# Exercise 2.6: Use break to stop loop when number is 5
# YOUR CODE HERE:



# Exercise 2.7: Use continue to skip number 5 in range 1-10
# YOUR CODE HERE:



# =============================================================================
# TOPIC 3: Functions & Lambda
# =============================================================================

# Exercise 3.1: Create a function that greets a person
# Function name: greet, parameter: name
# YOUR CODE HERE:



# Exercise 3.2: Create a function that returns the square of a number
# YOUR CODE HERE:



# Exercise 3.3: Create a function with default parameter
# Function: greet_with_message(name, message="Hello")
# YOUR CODE HERE:



# Exercise 3.4: Create a function that accepts *args and returns sum
# YOUR CODE HERE:



# Exercise 3.5: Create a function that accepts **kwargs and prints key-value pairs
# YOUR CODE HERE:



# Exercise 3.6: Lambda - Create a lambda to multiply two numbers
# YOUR CODE HERE:



# Exercise 3.7: Use lambda with map() to square all numbers in [1,2,3,4,5]
# YOUR CODE HERE:



# Exercise 3.8: Use lambda with filter() to get even numbers from [1,2,3,4,5,6,7,8,9,10]
# YOUR CODE HERE:



# Exercise 3.9: Use lambda with sorted() to sort list of tuples by second element
students = [("John", 85), ("Jane", 90), ("Bob", 78)]
# YOUR CODE HERE:



# =============================================================================
# TOPIC 4: Data Structures (Lists, Tuples, Sets, Dictionaries)
# =============================================================================

# Exercise 4.1: List operations
# Create a list with numbers 1-5, add 6 to end, insert 0 at beginning, remove 3
# YOUR CODE HERE:



# Exercise 4.2: List slicing
# From list [1,2,3,4,5,6,7,8,9,10], get:
# a) First 3 elements
# b) Last 3 elements
# c) Every second element
# d) Reverse the list
# YOUR CODE HERE:



# Exercise 4.3: List comprehension
# Create a list of squares of even numbers from 1-20
# YOUR CODE HERE:



# Exercise 4.4: Tuple unpacking
# Unpack tuple (10, 20, 30) into variables a, b, c
# YOUR CODE HERE:



# Exercise 4.5: Set operations
# Given sets a={1,2,3,4} and b={3,4,5,6}
# Find union, intersection, difference (a-b), symmetric difference
# YOUR CODE HERE:



# Exercise 4.6: Dictionary operations
# Create a dictionary with name, age, city. Add email, update age, remove city
# YOUR CODE HERE:



# Exercise 4.7: Dictionary comprehension
# Create a dictionary where keys are 1-5 and values are their squares
# YOUR CODE HERE:



# Exercise 4.8: Iterate over dictionary
# Print all key-value pairs from dictionary {"a": 1, "b": 2, "c": 3}
# YOUR CODE HERE:



# =============================================================================
# TOPIC 5: String Manipulation
# =============================================================================

# Exercise 5.1: String methods
# Given string "  Hello, World!  "
# a) Remove whitespace
# b) Convert to lowercase
# c) Convert to uppercase
# d) Replace "World" with "Python"
# YOUR CODE HERE:



# Exercise 5.2: String splitting and joining
# Split "apple,banana,cherry" by comma, then join with " - "
# YOUR CODE HERE:



# Exercise 5.3: String formatting
# Use f-string to format: name="John", age=30 -> "John is 30 years old"
# YOUR CODE HERE:



# Exercise 5.4: Check if string is palindrome
# Write code to check if "radar" is a palindrome (reads same forwards and backwards)
# YOUR CODE HERE:



# Exercise 5.5: Count occurrences of each character in a string
# For "hello world", count each character
# YOUR CODE HERE:



# =============================================================================
# TOPIC 6: File Handling
# =============================================================================

# Exercise 6.1: Write to a file
# Write 3 lines to a file named "test.txt"
# YOUR CODE HERE:



# Exercise 6.2: Read from a file
# Read the file created above and print its contents
# YOUR CODE HERE:



# Exercise 6.3: Append to a file
# Append a new line to "test.txt"
# YOUR CODE HERE:



# Exercise 6.4: Read file line by line
# Print each line from "test.txt" with line number
# YOUR CODE HERE:



# Exercise 6.5: JSON handling
# Create a dictionary and write it to a JSON file, then read it back
# YOUR CODE HERE:



# =============================================================================
# TOPIC 7: Object-Oriented Programming
# =============================================================================

# Exercise 7.1: Create a simple class
# Create a class 'Car' with attributes: brand, model, year
# Add a method 'display_info()' that prints car details
# YOUR CODE HERE:



# Exercise 7.2: Create objects from the class
# Create two Car objects and call display_info() on both
# YOUR CODE HERE:



# Exercise 7.3: Class with __init__ and __str__
# Create a class 'Rectangle' with width and height
# Add __str__ method to return "Rectangle(width, height)"
# YOUR CODE HERE:



# Exercise 7.4: Inheritance
# Create a class 'Animal' with name attribute and speak() method
# Create 'Dog' class that inherits Animal and overrides speak()
# YOUR CODE HERE:



# Exercise 7.5: Class methods and static methods
# Add a class method to count number of objects created
# Add a static method for utility function
# YOUR CODE HERE:



# =============================================================================
# TOPIC 8: Exception Handling
# =============================================================================

# Exercise 8.1: Basic try-except
# Write code that tries to divide by zero and catches the exception
# YOUR CODE HERE:



# Exercise 8.2: Multiple exceptions
# Handle both ValueError and ZeroDivisionError for division of user input
# YOUR CODE HERE:



# Exercise 8.3: Try-except-else-finally
# Demonstrate all four blocks
# YOUR CODE HERE:



# Exercise 8.4: Raise exception
# Write a function that raises ValueError if age < 0
# YOUR CODE HERE:



# Exercise 8.5: Custom exception
# Create a custom exception 'InvalidAgeError' and use it
# YOUR CODE HERE:



# =============================================================================
# TOPIC 9: Modules & Packages
# =============================================================================

# Exercise 9.1: Math module
# Use math module to calculate: sqrt(16), sin(pi/2), floor(3.7)
# YOUR CODE HERE:



# Exercise 9.2: Random module
# Generate: random float, random int 1-100, random choice from list
# YOUR CODE HERE:



# Exercise 9.3: Datetime module
# Print: current date, current time, date 7 days from now
# YOUR CODE HERE:



# Exercise 9.4: Collections module
# Use Counter to count words in "hello world hello python world"
# YOUR CODE HERE:



# Exercise 9.5: OS module
# Print: current directory, list files in current directory
# YOUR CODE HERE:



# =============================================================================
# TOPIC 10: Advanced Concepts (Decorators, Generators, Context Managers)
# =============================================================================

# Exercise 10.1: Simple decorator
# Create a decorator that prints "Before" and "After" the function call
# YOUR CODE HERE:



# Exercise 10.2: Timer decorator
# Create a decorator that measures and prints execution time
# YOUR CODE HERE:



# Exercise 10.3: Generator function
# Create a generator that yields even numbers up to n
# YOUR CODE HERE:



# Exercise 10.4: Generator expression
# Create a generator expression for squares of numbers 1-10
# YOUR CODE HERE:



# Exercise 10.5: Context manager
# Create a context manager that times a block of code
# YOUR CODE HERE:



# =============================================================================
# CHALLENGE EXERCISES
# =============================================================================

# Challenge 1: Flatten a nested list
# Convert [[1,2,3], [4,5], [6,7,8,9]] to [1,2,3,4,5,6,7,8,9]
# YOUR CODE HERE:



# Challenge 2: Find the most frequent element in a list
# YOUR CODE HERE:



# Challenge 3: Merge two dictionaries
# If same key exists, sum the values
# YOUR CODE HERE:



# Challenge 4: Implement a simple calculator class
# With methods: add, subtract, multiply, divide
# YOUR CODE HERE:



# Challenge 5: Read CSV file and find average of a column
# YOUR CODE HERE:



# =============================================================================
# TESTING YOUR CODE
# =============================================================================
# Run this file to test your solutions:
# python python_practice.py
# =============================================================================

print("\n" + "="*50)
print("PRACTICE COMPLETE!")
print("="*50)