def input_text():
    return input("Enter a paragraph of text: ")

# Task 1: Input Text
text = input_text()

def word_tokenization(text):
    return text.split()

# Task 2: Word Tokenization
words = word_tokenization(text)

def word_frequency_calculation(words):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

# Task 3: Word Frequency Calculation
word_freq = word_frequency_calculation(words)

def display_word_frequencies(word_freq):
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {freq} times")

# Task 4: Display Word Frequencies
display_word_frequencies(word_freq)

def top_n_words(word_freq, n):
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    for i in range(min(n, len(sorted_word_freq))):
        word, freq = sorted_word_freq[i]
        print(f"{word}: {freq} times")

# Task 5: Top N Words
n = int(input("Enter the value of N for top N words: "))
top_n_words(word_freq, n)

def word_search(word_freq, search_word):
    if search_word in word_freq:
        print(f"{search_word} appears {word_freq[search_word]} times.")
    else:
        print(f"{search_word} not found in the text.")

# Task 6: Word Search
search_word = input("Enter a word to search: ")
word_search(word_freq, search_word)
