'''
Write a Python program to merge two dictionaries. [may use: copy(), update()]
'''

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print("Merged Dictionary:", merged_dict)
