    
# Taking input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Checking conditions to find the greatest number''''<3
if a > b:
    if a > c:
        print(f"{a} is the greatest number.")
    elif a == c:
        print(f"{a} and {c} are the greatest numbers.")
    else:
        print(f"{c} is the greatest number.")
elif b > c:
    if b == a:
        print(f"{a} and {b} are the greatest numbers.")
    else:
        print(f"{b} is the greatest number.")
elif c == a:
    if c > b:
        print(f"{c} and {a} are the greatest numbers.")
    else:
        print(f"{b} is the greatest number.")
elif c == b:
    if c > a:
        print(f"{c} and {b} are the greatest numbers.")
    else:
        print(f"{a} is the greatest number.")
if a==b==c :
    print("all value are same ...")        
else:
    print(f"{c} is the greatest number.")
