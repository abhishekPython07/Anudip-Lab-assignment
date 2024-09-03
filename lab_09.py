
#1 . Write a Python program to Count all letters, digits, and special symbols from the given string

#  Input = “P@#yn26at^&i5ve” 


def count_characters(input_string):
    chars = 0  
    digits = 0  
    symbols = 0  
    # Loop through each character in the input string
    for char in input_string:
        if char.isalpha():  
            chars += 1
        elif char.isdigit(): 
            digits += 1
        else:  
            symbols += 1

    return chars, digits, symbols

input_string = "P@#yn26at^&i5ve"
chars, digits, symbols = count_characters(input_string)

print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")
# Output: Chars = 8 Digits = 3 Symbol =  4



# 2. Write a Python program to remove duplicate characters of a given string.

#  Input = “String and String Function” 
def remove_duplicates(input_string):
    seen = set()  
    output_string = [] 
    for char in input_string:
        if char not in seen:
            seen.add(char) 
            output_string.append(char)  

    return ''.join(output_string)
input_string = "String and String Function"

output_string = remove_duplicates(input_string)
print(output_string)


# Output: String and Function 



# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

#  Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 
def count_characters(input_string):
    uppercase = 0
    lowercase = 0
    numbers = 0
    special = 0
    for char in input_string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1  
            numbers += 1
        else: 
            special += 1

    # Return the counts
    return uppercase, lowercase, numbers, special
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"


uppercase, lowercase, numbers, special = count_characters(input_string)
print(f"UpperCase: {uppercase} LowerCase: {lowercase} NumberCase: {numbers} SpecialCase: {special}")



# Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11 


# 4. Write a Python Count vowels in a string 

# input= “Welcome to Python Assignment” 


def count_vowels(input_string):
    vowels = "aeiouAEIOU" 
    count = 0 
    for char in input_string:
        if char in vowels:  
            count += 1

    return count
input_string = "Welcome to Python Assignment"
vowel_count = count_vowels(input_string)
print(f"Total vowels are: {vowel_count}")


# Output: Total vowels are: 8



