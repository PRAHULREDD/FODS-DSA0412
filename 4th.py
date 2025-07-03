import numpy as np

# Sample quarterly sales data: [Q1, Q2, Q3, Q4]
sales_data = np.array([120000, 150000, 170000, 200000])

# Step 1: Total sales for the year
total_sales = np.sum(sales_data)

# Step 2: Percentage increase from Q1 to Q4
q1_sales = sales_data[0]
q4_sales = sales_data[3]

percentage_increase = ((q4_sales - q1_sales) / q1_sales) * 100

# Print results
print(f"Total sales for the year: ₹{total_sales}")
print(f"Percentage increase from Q1 to Q4: {percentage_increase:.2f}%")
