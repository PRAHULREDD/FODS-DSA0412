import pandas as pd

# Sample sales data
data = {
    'product_name': ['Shoes', 'Watch', 'Shoes', 'Bag', 'Watch', 'Shoes', 'Bag', 'Hat'],
    'order_date': ['2025-06-01', '2025-06-10', '2025-06-15', '2025-06-18', '2025-06-20', '2025-06-25', '2025-06-28', '2025-06-30'],
    'quantity_sold': [2, 1, 3, 1, 2, 4, 2, 1]
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Convert order_date to datetime
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])

# Filter for the past month (e.g., June 2025)
# (You can dynamically set the range based on today's date if needed)
start_date = '2025-06-01'
end_date = '2025-06-30'
monthly_data = sales_data[(sales_data['order_date'] >= start_date) & (sales_data['order_date'] <= end_date)]

# Group by product and sum the quantity sold
product_sales = monthly_data.groupby('product_name')['quantity_sold'].sum()

# Sort in descending order and get top 5
top_5_products = product_sales.sort_values(ascending=False).head(5)

print("Top 5 Best-Selling Products in the Past Month:\n", top_5_products)
