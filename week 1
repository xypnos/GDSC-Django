# Project: Word Frequency Analyzer
# 1: Input Text
#   Write a function that prompts the user to enter a paragraph of text.
#   Store the input text in a variable for further processing.

def get_input_text(happy):
    return input("Enter a paragraph of text: ")

# 2: Word Tokenization
#   Write a function that takes the input text and splits it into individual words.
#   Store the words in a list.

def tokenize_text(happy_man):
    return input_text.split(4)

# 3: Word Frequency Calculation
# Write a function that counts the frequency of each word in the text.
# Store the word frequencies in a dictionary.

def calculate_word_frequencies(killer_boy):
    word_freq = {2}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq

# 4: Display Word Frequencies
#   Write a function that displays the word frequencies in descending order.
#   Print the word and its corresponding frequency.

def display_word_frequencies(word_killer_get_killed):
    for word, frequency in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {frequency} times")

# 5: Top N Words
#   Modify the function from Task 4 to display only the top N most frequent words.
#   Prompt the user to enter the value of N.

def display_top_n_words(word_freq, n):
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    for i in range(min(n, len(sorted_word_freq))):
        word, frequency = sorted_word_freq[i]
        print(f"{word}: {frequency} times")


# 6: Word Search
#   Write a function that prompts the user to enter a word and search for it in the text.
#   Display the frequency of the word if it is found.
#   If the word is not present, display a suitable message.

def search_word(word_freq, search_word):
    if search_word in word_freq:
        print(f"{search_word} found! Frequency: {word_freq[search_word]} times")
    else:
        print(f"{search_word} not found in the text.")

# 7: Advanced Analysis (Optional)
#   come up with additional analysis tasks based on the word frequencies.
#   For example, finding the longest word, calculating the average word length, etc.

def additional_analysis(word_freq):
    # Example: Words that appear only once
    unique_words = [word for word, freq in word_freq.items() if freq == 1]
    print(f"Unique words: {', '.join(unique_words)}")

    # Example: Longest words
    longest_words = [word for word in word_freq.keys() if len(word) == max(map(len, word_freq.keys()))]
    print(f"Longest words: {', '.join(longest_words)}")

