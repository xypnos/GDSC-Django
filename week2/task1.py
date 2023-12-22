import re
from collections import Counter

def get_input_text():
    return input("Enter a paragraph of text: ")

def tokenize_words(input_text):
    return re.findall(r'\b\w+\b', input_text.lower())

def calculate_word_frequencies(words):
    return Counter(words)

def display_word_frequencies(word_frequencies):
    for word, frequency in word_frequencies.most_common():
        print(f"{word}: {frequency} times")

def display_top_n_words(word_frequencies, n):
    top_n_words = word_frequencies.most_common(n)
    for word, frequency in top_n_words:
        print(f"{word}: {frequency} times")

def search_word(word_frequencies):
    search_word = input("Enter a word to search: ")
    frequency = word_frequencies.get(search_word, 0)
    print(f"The word '{search_word}' appears {frequency} times." if frequency > 0 else f"The word '{search_word}' is not found.")