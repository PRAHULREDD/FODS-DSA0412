import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Example: Simulating sample data (remove this if you already have df)
# df = pd.read_csv("sales_data.csv")  # Uncomment and use your real data
df = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104, 105, 106, 107],
    'Age': [25, 30, 25, 40, 30, 25, 35],
    'Amount': [200, 150, 300, 400, 250, 350, 180]
})

# Step 1: Get the 'Age' column
ages = df['Age']

# Step 2: Calculate frequency distribution using value_counts()
age_freq = ages.value_counts().sort_index()

# Step 3: Display the frequency distribution
print("Frequency Distribution of Customer Ages:\n")
print(age_freq)

# Step 4: (Optional) Plot the frequency distribution
age_freq.plot(kind='bar', title='Customer Age Frequency Distribution', xlabel='Age', ylabel='Number of Purchases')
plt.tight_layout()
plt.show()
