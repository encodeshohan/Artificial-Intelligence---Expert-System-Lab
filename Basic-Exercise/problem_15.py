'''
Take a line of text (words separated by spaces) as input and find two words that have the highest and the lowest length.
'''

def find_longest_shortest_words(text):
    words = text.split()
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    return longest_word, shortest_word

text = input("Enter a line of text: ")
longest_word, shortest_word = find_longest_shortest_words(text)

print("Longest word:", longest_word)
print("Shortest word:", shortest_word)
