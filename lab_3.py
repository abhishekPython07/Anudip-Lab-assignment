#     Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

var = int( input(" Enter A number :  "))
if var%2==0:
    print ("Even number----")    
else:
    print( "odd number ----")


# 2.      Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.  

person= int(input( "checks whether a person is eligible to vote :   "))
if person>=18 :
    print("YES!   you are eligible for voting-----")
else :
    print("SORRY!   you are older--")    

# 3.      Write a Python program that determines if a given year is a leap year or not. 

    year= int(input("Enter A year checking for leap or not  :  "))
    if year%2==0 :
        print ( "Its leap year ,,,")
    else :
        print ("it is not a leap year  :")    

# 4.      Create a Python program that checks if a user-given number is positive, negative, or zero.

num= int(input("Enter a number :  "))
if num==0:
    print('its 0   ___-_____---__-_--')
elif num>0 :
    print("number is positive ")
else:
    print("number is negative")   



# 5.      Write a Python program that determines the largest of three numbers entered by the user 




    
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
