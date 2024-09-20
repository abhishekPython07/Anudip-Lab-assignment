# 1. Write a Python program to Get Only unique items from two sets. 
# Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 
# Define the input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_items = set1.union(set2)  
print(unique_items)  # Output the unique items

# Output: {70, 40, 10, 50, 20, 60, 30}






#  2. Write a Python program to Return a set of elements present in Set A or B, but not both. Input: 
# set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 

# Define the input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_elements = set1.symmetric_difference(set2)
print(unique_elements)

# Output: {20, 70, 10, 60}