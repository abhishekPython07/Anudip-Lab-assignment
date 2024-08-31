# To Find Number of all letters, digits, and special symbols
txt = input("Enter Some String")  # Python PRogramming 2 Data Analyst@MyStudents!
print("Given String", txt)
n = len(txt)
print(n)
chars = 0
digits = 0
symbols = 0

for i in range(0, n):
    if txt[i].isalpha():
        chars += 1
    elif txt[i].isdigit():
        digits += 1
    else:
        symbols += 1

print("Total Number of Letters:", chars)
print("Total Number of Digits:", digits)
print("Total Number of Symbols:", symbols)
