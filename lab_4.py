
# 1.     Function without Parameters:
def function ():
    print("hello")


function()

# 2.      Function with Parameter:
def function_02(a, b):
    result = a + b
    return result

result_ = function_02(3, 4)
print(result_)




# 3.      Function with Default Parameter:
def function(l, w):
    area = l * w
    return area

l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))

result_area = function(l, w)

print(f"The area of a rectangle with length {l} and width {w} is: {result_area}")

# # 4.      Function with Return Keyword:

# # 5.      Recursion
def fibonacci_sequence(n):
    # Initialize the first two terms of the sequence
    fib_sequence = [0, 1]
    
    # Generate subsequent terms of the sequence
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

# Example usage: Generate Fibonacci sequence up to 10 terms
n_terms = 10
fib_sequence = fibonacci_sequence(n_terms)
print(f"The Fibonacci sequence up to {n_terms} terms: {fib_sequence}")
