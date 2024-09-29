# 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.full(10, 5)

print("Array of 10 zeros:", zeros_array)
print("Array of 10 ones:", ones_array)
print("Array of 10 fives:", fives_array)

#Output:Array of 10 zeros: 
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Array of 10 ones: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
# Array of 10 fives: [5 5 5 5 5 5 5 5 5 5]







# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 matrix with values from 2 to 10:\n", matrix)

#Output:
# 3x3 matrix with values from 2 to 10:
#  [[ 2  3  4]
#  [ 5  6  7]
#  [ 8  9 10]]







# 3. Write a NumPy program to create an array with values ranging from 12 to 38.
import numpy as np

array_range = np.arange(12, 39)
print("Array with values from 12 to 38:", array_range)
#Output:
# Array with values from 12 to 38: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
#  36 37 38]







# 4. Write a NumPy program to convert a list and tuple into arrays. Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8] 
import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

array_from_list = np.array(my_list)
array_from_tuple = np.array(my_tuple)

print("Array from list:", array_from_list)
print("Array from tuple:\n", array_from_tuple)

#Output:
# Array from list: [1 2 3 4 5 6 7 8]
# Array from tuple:
#  [[8 4 6]
#  [1 2 3]]
