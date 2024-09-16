# 1. Write a Python program to sum all the items in a list.

# List of items
my_list = [10, 20, 30, 40, 50, 60]
total_sum = sum(my_list)
print(f"The sum of all items in the list: {total_sum}")

#output : The sum of all items in the list: 210







# 2.Write a Python program to traverse a given list in reverse order, and print the elements with the original index. 

my_list2 = ['red', 'green', 'white', 'black']

print(" withou Traverse the list in reverse order:",my_list2 )
print("Traverse the list in reverse order:")
for i in range(len(my_list2)-1, -1, -1):
    print(f"Index {i}, Element: {my_list2[i]}")

#output: withou Traverse the list in reverse order: ['red', 'green', 'white', 'black']
# Traverse the list in reverse order:
# Index 3, Element: black
# Index 2, Element: white
# Index 1, Element: green
# Index 0, Element: red
# PS D:\PYTHON> 








