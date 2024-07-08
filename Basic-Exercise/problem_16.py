'''
Write a Python program to get the largest and the smallest number from a list.
'''

def get_largest_smallest(lst):
    if len(lst) < 1:
        return None
    else:
        largest = max(lst)
        smallest = min(lst)
        return largest, smallest

numbers = [10, 5, 7, 200, 96, 80, 48]
largest, smallest = get_largest_smallest(numbers)

print("Largest number is: ", largest)
print("Smallest number is: ", smallest)
