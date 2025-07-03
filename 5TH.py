import numpy as np

# Sample dataset: fuel efficiency (in mpg) of different car models
fuel_efficiency = np.array([25, 30, 28, 32, 35, 27, 22])

# 1. Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency, "mpg")

# 2. Calculate percentage improvement between two car models
# Example: Model A at index 0, Model B at index 4
model_a = fuel_efficiency[0]  # Old model: 25 mpg
model_b = fuel_efficiency[4]  # New model: 35 mpg

# Percentage Improvement Formula
improvement = ((model_b - model_a) / model_a) * 100
print("Percentage Improvement from Model A to Model B:", improvement, "%")
