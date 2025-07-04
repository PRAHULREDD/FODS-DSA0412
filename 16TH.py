import pandas as pd
import string
from collections import Counter

# Example DataFrame (replace this with your actual data source)
# df = pd.read_csv("reviews.csv")  # Load from a CSV file if needed
df = pd.DataFrame({
    'Review': [
        "Great product, loved it!",
        "The product is good but could be better.",
        "I didn't like the product at all.",
        "Excellent quality and fast delivery!",
        "Good value for money."
    ]
})

# Step 1: Combine all reviews into a single text
all_reviews = ' '.join(df['Review'].astype(str))

# Step 2: Convert text to lowercase
all_reviews = all_reviews.lower()

# Step 3: Remove punctuation
all_reviews = all_reviews.translate(str.maketrans('', '', string.punctuation))

# Step 4: Tokenize text (split into words)
words = all_reviews.split()

# Step 5: Count word frequencies
word_freq = Counter(words)

# Step 6: Display frequency distribution
print("Word Frequency Distribution:\n")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
