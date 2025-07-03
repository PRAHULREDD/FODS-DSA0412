import pandas as pd

# Sample data
property_data = pd.DataFrame({
    'property_id': [101, 102, 103, 104, 105],
    'location': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai'],
    'bedrooms': [2, 3, 4, 5, 3],
    'area_sqft': [1200, 1000, 1800, 2200, 950],
    'listing_price': [6000000, 8500000, 9500000, 12000000, 7800000]
})

# 1. Average price by location
print("Avg price by location:\n", property_data.groupby('location')['listing_price'].mean())

# 2. Properties with more than 3 bedrooms
print("\n>3 bedroom properties:\n", property_data[property_data['bedrooms'] > 3])

# 3. Most expensive property
print("\nMost expensive:\n", property_data.loc[property_data['listing_price'].idxmax()])

# 4. Area per bedroom
property_data['area/bedroom'] = property_data['area_sqft'] / property_data['bedrooms']
print("\nArea per bedroom:\n", property_data[['property_id', 'area/bedroom']])

# 5. Properties priced between ₹50L and ₹1Cr
print("\n₹50L–₹1Cr properties:\n", property_data[
    (property_data['listing_price'] >= 5000000) &
    (property_data['listing_price'] <= 10000000)
])
