import matplotlib.pyplot as plt

# Sample sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [10000, 12000, 9000, 15000, 14000, 17000]

# 1. Line Plot
plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker='o', linestyle='-', color='blue')
plt.title('Monthly Sales (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(months, sales, color='red')
plt.title('Monthly Sales (Scatter Plot)')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Bar Plot
plt.figure(figsize=(6, 4))
plt.bar(months, sales, color='green')
plt.title('Monthly Sales (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.tight_layout()
plt.show()
