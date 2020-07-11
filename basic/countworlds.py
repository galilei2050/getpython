import collections
import string
import random


FILE_NAME='war-and-peace.txt'


# Create dict with world statistics
# Dict is key-value structure
words_stat = dict()

# Open file for reading
# We use with context manager to guarantee that file will be close after exit from context expression
with open(FILE_NAME) as input_file:
    for line in input_file.readlines():
        # Line is the sequence of letters. Let's split it to the list of words.
        words = line.replace('—', ' ').split(' ')
        for word in words:
            word = word.strip(string.punctuation + '””—').strip('\n').lower()
            if word not in words_stat:
                words_stat[word] = 0
            words_stat[word] += 1

# Size of
unique_words = len(words_stat.keys())
total_words = sum(words_stat.values())
print(f"Total/unique words {total_words}/{unique_words} in file {FILE_NAME}")

# Create list of paris like [(word1, 123), (word2, 321), ... ]
freq_pairs = list(words_stat.items())

# 10 Random frequency
print("Random frequencies")
for i in range(1, 11):
    # Pick random index
    random_word = random.randrange(0, unique_words)
    # Print random world freq
    word, freq = freq_pairs[random_word]
    print(f"# {i:1d} - '{word}' occur {freq} times")

# Reverse word frequency
stat_words = {frequency: word for word, frequency in words_stat.items()}
ten_frequent = sorted(stat_words.keys(), reverse=True)[:10]

print("Most frequent worlds")
for i, freq in enumerate(ten_frequent):
    word = stat_words[freq]
    print(f"# {i:1d} - '{word}' occur {freq} times")
