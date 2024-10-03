import pandas as pd


class StudentDataAnalyzer:
    def __init__(self, csv_file, subjects_list):
        self.df = pd.read_csv(csv_file)
        self.subjects = subjects_list

    def clean_data(self):
        self.df.dropna()

    def get_failed_students(self):
        return self.df[self.df[self.subjects].lt(50).any(axis=1)]['Student'].unique()

    def get_avg_semester_scores(self):
        return self.df.groupby('Semester')[self.subjects].mean()

    def get_highest_avg_student(self):
        df = self.df
        df['Average_Score'] = df[self.subjects].mean(axis=1)
        highest_student = df.groupby(
            'Student')['Average_Score'].mean().idxmax()
        return highest_student

    def get_hardest_subject(self):
        average_subject_scores = self.df[self.subjects].mean()
        hardest_subject = average_subject_scores.idxmin()
        return hardest_subject

    def get_average_total_scores(self):
        df = self.df
        df['Total_Score'] = df[self.subjects].sum(axis=1)
        average_total = df.groupby('Semester')['Total_Score'].mean()
        return average_total

    def get_improving_students(self):
        self.df['Average_Score'] = self.df[self.subjects].mean(axis=1)
        student_scores = self.df.groupby(['Student', 'Semester'])[
            'Average_Score'].mean().reset_index()

        # calculate the difference between the average score of the current semester and the previous semester
        student_scores['Score_Difference'] = student_scores.groupby('Student')[
            'Average_Score'].diff()

        # find the students who have all score differences >= 0
        improved_students = student_scores.groupby(
            'Student')['Score_Difference'].min()
        improved_students = improved_students[improved_students >= 0].index.tolist(
        )

        return improved_students
