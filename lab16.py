
# 1. Convert the below list into numpy array then display the array

#  Input: my_list = [1, 2, 3, 4, 5] 
import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("Numpy Array:", my_array)

#output: Numpy Array: [1 2 3 4 5]





# 2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

#  Input: my_list = [1, 2, 3, 4, 5]
import numpy as np

list = [1, 2, 3, 4, 5]
array = np.array(list)

print("Numpy Array:", array)

print("First element:", array[0])
print("Last element:", array[-1])

multiplied_array = array * 2
print("Array after multiplying by 2:", multiplied_array)


#output: 
#  First element: 1
# Last element: 5
# Array after multiplying by 2: [ 2  4  6  8 10]