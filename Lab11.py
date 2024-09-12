# . Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero. 
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#output
# Enter the numerator: 2
# Enter the denominator: 0
# Error: Division by zero is not allowed.
# Enter an integer


# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. 
try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print("Error: Input is not a valid integer.")

    #output
#     Enter an integer: abhishek
# Error: Input is not a valid integer.

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. 
try:
    file_name = input("Enter the file name to open: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")

#output
    # Enter the file name to open: Abhishek.txt
# Error: The file does not exist.

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if not (num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numerical.")
    result = float(num1) + float(num2)
    print(f"The sum is: {result}")
except TypeError as e:
    print(f"Error: {e}")

#output


