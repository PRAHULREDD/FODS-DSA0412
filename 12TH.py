import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [12, 14, 18, 22, 28, 32, 30, 29, 26, 20, 16, 13]  # In °C
rainfall = [45, 30, 25, 20, 10, 5, 20, 25, 30, 40, 50, 60]      # In mm

# 1. Line Plot for Temperature
plt.figure(figsize=(8, 4))
plt.plot(months, temperature, marker='o', color='orange')
plt.title('Monthly Temperature (°C)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Scatter Plot for Rainfall
plt.figure(figsize=(8, 4))
plt.scatter(months, rainfall, color='blue')
plt.title('Monthly Rainfall (mm)')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.tight_layout()
plt.show()
