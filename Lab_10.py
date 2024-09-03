
# 1. Write a function in python to read the content 
# from a text file "ABC.txt" line by line and display the same on screen. 

def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='') 
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "ABC.txt"
read_file_line_by_line(filename)


# OutpuT
# Hello, world!

# Here's a Python function that reads a text file named "ABC.txt" and counts the total number of words in the file:
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()  
            word_count = len(words)
            print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
count_words_in_file('ABC.txt')
# Output
# Total number of words in 'ABC.txt': 2


# 3. Write a function in Python to count uppercase character in a text file “ABC.txt”
def count_uppercase_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper()) 
            print(f"Total number of uppercase characters in '{filename}': {uppercase_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
count_uppercase_characters('ABC.txt')   


#  4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split() 
                short_words = [word for word in words if len(word) < 4]
                print(" ".join(short_words))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

display_words('story.txt')   
