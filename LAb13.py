# 1. Write a Python script to concatenate the following dictionaries to create a new one. 
# Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Using update() method
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print("Concatenated dictionary:", new_dict)
new_dict = {**dic1, **dic2, **dic3}
print("Concatenated dictionary New:", new_dict)

#Output
# Concatenated dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Concatenated dictionary New: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}









# 2. Write a Python program to get the key, value and item in a dictionary.
#  input: dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for key, value in dict_num.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}: {value})")

#Output
# Key: 1, Value: 10, Item: (1: 10)
# Key: 2, Value: 20, Item: (2: 20)
# Key: 3, Value: 30, Item: (3: 30)
# Key: 4, Value: 40, Item: (4: 40)
# Key: 5, Value: 50, Item: (5: 50)
# Key: 6, Value: 60, Item: (6: 60)