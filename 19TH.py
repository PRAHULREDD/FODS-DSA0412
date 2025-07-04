import numpy as np
import scipy.stats as stats

# Sample data (replace with your actual results)
# Assume each group has 25 patients
np.random.seed(0)
drug_group = np.random.normal(loc=10, scale=5, size=25)       # mean=10, std=5
placebo_group = np.random.normal(loc=3, scale=4, size=25)     # mean=3, std=4

def compute_confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)
    t_score = stats.t.ppf((1 + confidence) / 2, df=n-1)
    margin_of_error = t_score * std_err
    ci_lower = mean - margin_of_error
    ci_upper = mean + margin_of_error
    return mean, (ci_lower, ci_upper)

# Calculate CI for both groups
drug_mean, drug_ci = compute_confidence_interval(drug_group)
placebo_mean, placebo_ci = compute_confidence_interval(placebo_group)

# Display results
print(f"Drug Group - Mean Reduction: {drug_mean:.2f}, 95% CI: ({drug_ci[0]:.2f}, {drug_ci[1]:.2f})")
print(f"Placebo Group - Mean Reduction: {placebo_mean:.2f}, 95% CI: ({placebo_ci[0]:.2f}, {placebo_ci[1]:.2f})")
