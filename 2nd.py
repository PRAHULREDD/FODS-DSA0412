import numpy as np
sales_data = np.array([
    [200, 220, 210],
    [150, 160, 170],   
    [300, 310, 110]    
])

average_price = np.mean(sales_data)
print(f"Average price of all products sold: ₹{average_price:.2f}")
