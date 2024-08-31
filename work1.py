# To Find Number of Upper case, lower case, Special Symbols and Digits
txt = input("Enter Some String")  # Python PRogramming 2 Data Analyst@MyStudents!
print("Given String", txt)
n = len(txt)
print(n)
upper = 0
lower = 0
space = 0
digit = 0
sym = 0

for i in range(0, n):
    if txt[i] >= 'A' and txt[i] <= 'Z':
        upper += 1
    elif txt[i] >= 'a' and txt[i] <= 'z':
        lower += 1
    elif txt[i] == ' ':
        space += 1
    elif txt[i] >= '0' and txt[i] <= '9':
        digit += 1
    else:
        sym += 1

print("Total Number of Upper case:", upper)
print("Total Number of Lower case:", lower)
print("Total Number of space:", space)
print("Total Number of digit:", digit)
print("Total Number of sym:", sym)
