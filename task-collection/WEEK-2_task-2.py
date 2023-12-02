def inputwords():
    x=input("Enter list of words as a paragraph here: ")
    return x.split()
#start
words=inputwords()

def calculate_word_lengths(words):
    return [len(word) for word in words]

# Task 1: Calculate Word Lengths
word_lengths = calculate_word_lengths(words)

def average_word_length(word_lengths):
    if not word_lengths:
        return 0
    return sum(word_lengths) / len(word_lengths)

# Task 2: Average Word Length
avg_length = average_word_length(word_lengths)
print(f"Average Word Length: {avg_length:.2f} characters")

def longest_word(words):
    if not words:
        return None, 0
    
    longest = max(words, key=len)
    return longest, len(longest)

# Task 2: Average Word Length
avg_length = average_word_length(word_lengths)
print(f"Average Word Length: {avg_length:.2f} characters")

def shortest_word(words):
    if not words:
        return None, 0
    
    shortest = min(words, key=len)
    return shortest, len(shortest)

# Task 3: Longest Word
longest, longest_length = longest_word(words)
print(f"Longest Word: {longest}, Length: {longest_length} characters")

# Task 4: Shortest Word
shortest, shortest_length = shortest_word(words)
print(f"Shortest Word: {shortest}, Length: {shortest_length} characters")

def word_length_distribution(words):
    word_length_freq = {}
    for word in words:
        length = len(word)
        word_length_freq[length] = word_length_freq.get(length, 0) + 1
    return word_length_freq

# Task 5: Word Length Distribution
word_length_freq = word_length_distribution(words)

def display_word_length_distribution(word_length_freq):
    for length, freq in sorted(word_length_freq.items()):
        print(f"Word length {length}: {freq} times")

# Task 6: Display Word Length Distribution
display_word_length_distribution(word_length_freq)
