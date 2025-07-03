import numpy as np

# Example house data: [Bedrooms, Square Footage, Sale Price]
house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 400000],
    [4, 1800, 300000],
    [6, 3500, 550000],
    [5, 2800, 480000],
    [2, 1200, 200000]
])

# Step 1: Filter rows where bedrooms > 4
houses_with_more_than_4_bedrooms = house_data[house_data[:, 0] > 4]

# Step 2: Extract the sale prices (column index 2)
sale_prices = houses_with_more_than_4_bedrooms[:, 2]

# Step 3: Calculate the average sale price
average_price = np.mean(sale_prices)

print(f"Average sale price of houses with more than 4 bedrooms: ₹{average_price:.2f}")
