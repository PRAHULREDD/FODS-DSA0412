import numpy as np
from scipy import stats

# Example: Simulated conversion rate data (you should replace this with actual data)
# Let's assume conversion rates are in percentage (e.g., 5.2%)
np.random.seed(42)
design_a = np.random.normal(loc=4.5, scale=1.2, size=100)  # 100 users saw Design A
design_b = np.random.normal(loc=5.1, scale=1.1, size=100)  # 100 users saw Design B

# Step 1: Perform independent t-test (equal_var=False for Welch’s t-test)
t_stat, p_value = stats.ttest_ind(design_a, design_b, equal_var=False)

# Step 2: Display results
print("A/B Test Results:")
print(f"Mean Conversion Rate - Design A: {np.mean(design_a):.2f}%")
print(f"Mean Conversion Rate - Design B: {np.mean(design_b):.2f}%")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Step 3: Conclusion
alpha = 0.05
if p_value < alpha:
    print("✅ Result: Statistically significant difference in conversion rates (reject H₀)")
else:
    print("❌ Result: No statistically significant difference (fail to reject H₀)")
