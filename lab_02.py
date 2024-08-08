# Q.1 Write a program for arithmatic operators


# Take two numbers from the user
num2 = int(input("Enter the second number: "))
num1 = int(input("Enter the first number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulo = num1 % num2
exponentiation = num1 ** num2

# Display the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulo: {num1} % {num2} = {modulo}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")





# Q.2 Write a program for assignment operators

a = 10
b = 5

# Display initial values
print(f"Initial values: a = {a}, b = {b}")

# Assignment operator: =
a = 10
print(f"After a = 10: a = {a}")

# Add and assign: +=
a += 5  
print(f"After a += 5: a = {a}")

# Subtract and assign: -=
b -= 3  
print(f"After b -= 3: b = {b}")

# Multiply and assign: *=
a *= 2  
print(f"After a *= 2: a = {a}")

# Divide and assign: /=
b /= 2  
print(f"After b /= 2: b = {b}")

# Modulus and assign: %=
a %= 3  
print(f"After a %= 3: a = {a}")

# Exponentiation and assign: **=
b **= 2  
print(f"After b **= 2: b = {b}")





# Q.3Write a program for Bitwise operators 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Bitwise AND (&)
bitwise_and = num1 & num2
print(f"Bitwise AND: {num1} & {num2} = {bitwise_and}")

# Bitwise OR (|)
bitwise_or = num1 | num2
print(f"Bitwise OR: {num1} | {num2} = {bitwise_or}")

# Bitwise XOR (^)
bitwise_xor = num1 ^ num2
print(f"Bitwise XOR: {num1} ^ {num2} = {bitwise_xor}")

# Bitwise NOT (~) of num1
bitwise_not_num1 = ~num1
print(f"Bitwise NOT (~{num1}): {bitwise_not_num1}")







# Q.4 Write a program to calculate greatest of three numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")





# 1.      Calculate the area of a circle.
import math


radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)

print(f"The area of a circle with radius {radius} is: {area}")





# 2.      Calculate the area of a triangle.

base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Print the area of the triangle
print(f"The area of a triangle with base {base} and height {height} is: {area}")





# 3.      Calculate the area of a rectangle.

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

# Print 
print(f"The area of a rectangle with length {length} and width {width} is: {area}")




# 4.      Calculate the area of a square.

side = float(input("Enter the side length of the square: "))

area = side ** 2

print(f"The area of a square with side length {side} is: {area}")


