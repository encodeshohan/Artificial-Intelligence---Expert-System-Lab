# -*- coding: utf-8 -*-
"""problem_17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lt8YcK__kN959IsS4btdCguARtQiW_n1
"""

'''
Write a Python program to print a specified list after removing the elements from some specific positions such as removing 0th, 4th and 5th elements from a list of length 6.
'''

def remove_elements(lst, positions):
    for pos in sorted(positions, reverse=True):
        del lst[pos]
    return lst

numbers = [10, 20, 30, 40, 50, 60]
positions_to_remove = [0, 4, 5]

new_list = remove_elements(numbers, positions_to_remove)

print("Original list:", [10, 20, 30, 40, 50, 60])
print("List after removing elements at positions ", positions_to_remove, " : ", new_list)