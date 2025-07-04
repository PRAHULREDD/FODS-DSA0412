import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm

# Step 1: Input data (example for 18 adults)
data = {
    'Age': [23, 25, 28, 32, 35, 37, 40, 42, 44, 45, 47, 48, 50, 52, 53, 55, 57, 60],
    'Fat': [15.1, 16.3, 17.2, 18.0, 19.5, 20.2, 21.4, 22.0, 22.5, 23.0, 23.3, 24.1, 24.5, 25.0, 25.2, 26.3, 27.0, 28.1]
}

df = pd.DataFrame(data)

# Step 2: Mean, Median, Std Deviation
print("Descriptive Statistics:\n")
print("Age:")
print(f"Mean: {df['Age'].mean():.2f}")
print(f"Median: {df['Age'].median():.2f}")
print(f"Standard Deviation: {df['Age'].std():.2f}\n")

print("Body Fat (%):")
print(f"Mean: {df['Fat'].mean():.2f}")
print(f"Median: {df['Fat'].median():.2f}")
print(f"Standard Deviation: {df['Fat'].std():.2f}\n")

# Step 3: Boxplots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['Age'], color='lightblue')
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Fat'], color='lightgreen')
plt.title('Boxplot of %Fat')

plt.tight_layout()
plt.show()

# Step 4: Scatter Plot
plt.figure(figsize=(6, 5))
sns.scatterplot(x='Age', y='Fat', data=df, color='darkblue')
plt.title('Scatter Plot of Age vs. %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.grid(True)
plt.show()

# Step 5: Q-Q Plot for Age and Fat
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sm.qqplot(df['Age'], line='s', ax=plt.gca())
plt.title('Q-Q Plot of Age')

plt.subplot(1, 2, 2)
sm.qqplot(df['Fat'], line='s', ax=plt.gca())
plt.title('Q-Q Plot of %Fat')

plt.tight_layout()
plt.show()
