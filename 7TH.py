import pandas as pd

# Sample dataset
data = {
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2024-01-01', '2024-01-05', '2024-02-10', '2024-03-15', '2024-04-20', '2024-05-25'],
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet'],
    'order_quantity': [1, 2, 1, 1, 3, 2]
}

# Create DataFrame
order_data = pd.DataFrame(data)

# Convert order_date column to datetime
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# 1. Total number of orders made by each customer
orders_per_customer = order_data['customer_id'].value_counts()
print("1. Total number of orders per customer:\n", orders_per_customer)

# 2. Average order quantity for each product
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
print("\n2. Average order quantity per product:\n", avg_quantity_per_product)

# 3. Earliest and latest order dates
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()
print("\n3. Earliest Order Date:", earliest_date)
print("   Latest Order Date:", latest_date)
