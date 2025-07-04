import string
from collections import Counter

# Step 1: Read the text from the file
with open("sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Step 2: Convert text to lowercase
text = text.lower()

# Step 3: Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 4: Split text into words (tokenization)
words = text.split()

# Step 5: Count word frequency using Counter
word_freq = Counter(words)

# Step 6: Display the frequency distribution
print("Word Frequency Distribution:\n")
for word, freq in word_freq.most_common():  # You can limit with [:10] for top 10
    print(f"{word}: {freq}")
