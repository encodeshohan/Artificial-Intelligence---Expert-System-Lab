'''
Take an integer value as input and determine whether it is an even or odd number. Therefore, print an appropriate message (even/odd).
'''

num = int(input("Enter an Integer: "))

if num % 2 == 0:
    print(num, "is EVEN!.")
else:
    print(num, "is ODD!.")
