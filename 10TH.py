import matplotlib.pyplot as plt

# Sample monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [15000, 18000, 12000, 22000, 21000, 25000]

# 1. Line Plot
plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker='o', color='blue', linestyle='-')
plt.title('Monthly Sales - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Plot
plt.figure(figsize=(8, 4))
plt.bar(months, sales, color='green')
plt.title('Monthly Sales - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.tight_layout()
plt.show()
