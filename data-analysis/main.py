import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('student_scores_random_names.csv')
# df.dropna()

print(df.head())

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
failed_students = df[df[subjects].lt(50).any(axis=1)]['Student'].unique()
print(failed_students)

average_semester_scores = df.groupby('Semester')[subjects].mean()
print(average_semester_scores)

df['Average_Score'] = df[subjects].mean(axis=1)
highest_average_score_student = df.groupby(
    'Student')['Average_Score'].mean().idxmax()
print(highest_average_score_student)

average_subject_scores = df[subjects].apply(np.mean)
hardest_subject = average_subject_scores.idxmin()
print(hardest_subject)


average_semester_scores.reset_index().to_excel(
    'average_scores_per_semester.xlsx', index=False)

average_semester_scores.plot(kind='bar', figsize=(10, 7))
plt.title('Average Scores by Subject for All Semesters')
plt.xlabel('Semester')
plt.ylabel('Average Score')
plt.legend(title='Subjects', loc='upper left')

df['Total_Score'] = df[subjects].sum(axis=1)
average_total_scores = df.groupby('Semester')['Total_Score'].mean()

plt.figure()
average_total_scores.plot(kind='line', figsize=(10, 7), marker='o')
plt.title('Average Total Score per Semester')
plt.xlabel('Semester')
plt.ylabel('Average Total Score')
plt.grid(True)
plt.show()
