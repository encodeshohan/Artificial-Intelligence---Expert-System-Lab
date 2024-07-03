'''
Write a Python program to swap the values of two variables. Try this exercise with and without using a function.
'''

# Without using a function
a = 10
b = 20
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)


# Using a function
def swap(x, y):
    return y, x
a = 10
b = 20
print("Before swapping: a =", a, ", b =", b)
a, b = swap(a, b)
print("After swapping: a =", a, ", b =", b)
