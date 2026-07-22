# Day 2 - Python Basics
# Topics: Variables, Data Types, Operators, Loops, Functions
# 1. Variables
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)


# 2. Data Types

x = 10                                   # int
y = 3.14                                 # float
z = "hello"                              # str
flag = True                              # bool
fruits = ["apple", "banana", "mango"]    # list
coords = (10, 20)                        # tuple
person = {"name": "Alice", "age": 25}    # dict
unique_nums = {1, 2, 3}                  # set

print(type(x), type(y), type(z), type(flag))

# 3. Operators
a, b = 10, 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

print(a > b, a == b, a != b)
print(a > 5 and b < 5, a > 5 or b > 5, not (a > 5))


# 4. Loops

print("For loop:")
for i in range(1, 6):
    print(i)

print("While loop:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("Loop through list:")
for fruit in fruits:
    print(fruit)


# 5. Functions
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

print(greet("Alice"))
print(add(4, 5))
print(is_even(10))


# 6. Practice Programs

# a) Sum of numbers 1 to N
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of 1 to", n, "is", total)

# b) Largest number in a list
numbers = [12, 45, 7, 89, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)

# c) Check for prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 26 prime?", is_prime(26))
print("Is 7 prime?", is_prime(7))