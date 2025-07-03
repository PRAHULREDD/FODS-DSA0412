import numpy as np

# 4x4 matrix: Rows = students, Columns = subjects (Math, Science, English, History)
student_scores = np.array([
    [85, 90, 78, 92],   # Student 1
    [88, 76, 85, 80],   # Student 2
    [90, 82, 89, 85],   # Student 3
    [70, 88, 92, 78]    # Student 4
])

# Subject names
subjects = ['Math', 'Science', 'English', 'History']

# Step 1: Calculate average score for each subject (column-wise mean)
average_scores = np.mean(student_scores, axis=0)

# Step 2: Display average score for each subject
for subject, avg in zip(subjects, average_scores):
    print(f"Average score in {subject}: {avg:.2f}")

# Step 3: Identify subject with highest average score
max_index = np.argmax(average_scores)
print(f"\nSubject with the highest average score: {subjects[max_index]} ({average_scores[max_index]:.2f})")
