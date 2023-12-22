def calculate_word_lengths(words):
    return [len(word) for word in words]

def calculate_average_word_length(word_lengths):
    return sum(word_lengths) / len(word_lengths) if word_lengths else 0

def find_longest_word(words):
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

def find_shortest_word(words):
    shortest_word = min(words, key=len)
    return shortest_word, len(shortest_word)

def calculate_word_length_distribution(word_lengths):
    from collections import Counter
    return Counter(word_lengths)

def display_word_length_distribution(length_distribution):
    for length, frequency in sorted(length_distribution.items()):
        print(f"Word length {length}: {frequency} words")

# illustrations

words = ["apple", "banana", "kiwi", "orange", "grape"]
word_lengths = calculate_word_lengths(words)

average_length = calculate_average_word_length(word_lengths)
print(f"Average Word Length: {average_length:.2f} characters")

longest_word, longest_length = find_longest_word(words)
print(f"Longest Word: {longest_word} (Length: {longest_length} characters)")

shortest_word, shortest_length = find_shortest_word(words)
print(f"Shortest Word: {shortest_word} (Length: {shortest_length} characters)")

length_distribution = calculate_word_length_distribution(word_lengths)
print("\nWord Length Distribution:")
display_word_length_distribution(length_distribution)