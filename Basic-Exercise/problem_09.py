'''
Write a Python program that accepts a filename from the user and prints the extension of the file.
'''

fileName = input("Enter a filename: ")
if '.' in fileName:
    extension = fileName.split('.')[-1]
    print("File extension:", extension)
else:
    print("Invalid filename.")