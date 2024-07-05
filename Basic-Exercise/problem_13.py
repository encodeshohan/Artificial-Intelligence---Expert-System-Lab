'''
Write a Python program to find the total number of even and odd numbers from a given list.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def count_even_odd(numbers):
    even_count = len([num for num in numbers if num % 2 == 0])
    odd_count = len(numbers) - even_count
    return even_count, odd_count

even_count, odd_count = count_even_odd(numbers)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
