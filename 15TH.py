import pandas as pd
import matplotlib.pyplot as plt

# Example dataset (remove this if you're loading from a real file)
# df = pd.read_csv("interactions.csv")  # Load actual data from CSV
df = pd.DataFrame({
    'PostID': [1, 2, 3, 4, 5, 6, 7],
    'Likes': [10, 15, 10, 20, 15, 10, 5]
})

# Step 1: Extract the Likes column
likes = df['Likes']

# Step 2: Calculate frequency distribution using value_counts()
likes_freq = likes.value_counts().sort_index()

# Step 3: Display the frequency distribution
print("Frequency Distribution of Likes:\n")
print(likes_freq)

# Step 4: Optional - Plot the distribution as a bar chart
likes_freq.plot(kind='bar', title='Frequency Distribution of Likes', xlabel='Likes', ylabel='Number of Posts')
plt.tight_layout()
plt.show()
