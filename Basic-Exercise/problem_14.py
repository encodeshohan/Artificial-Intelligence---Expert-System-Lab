'''
Write a Python program that will sort the numbers of a given list in both ascending and descending order without modifying the original (given) list.
'''



def sort_list(numbers):
    numbers_copy = numbers.copy()

    ascending_sorted = sorted(numbers_copy)

    descending_sorted = sorted(numbers_copy, reverse=True)

    return ascending_sorted, descending_sorted

numbers = [64, 34, 25, 12, 22, 11, 90]
ascending_sorted, descending_sorted = sort_list(numbers)

print("Original list:", numbers)
print("Ascending order:", ascending_sorted)
print("Descending order:", descending_sorted)