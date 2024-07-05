'''
Take a character as input and determine whether it is a vowel or not. Therefore, print an appropriate message (vowel/not vowel).
'''

char = input("Enter a Character: ")
vowels = ['a', 'e', 'i', 'o', 'u']
if char.lower() in vowels:
    print(char, "is a VOWEL.")
else:
    print(char, "is not a VOWEL.")