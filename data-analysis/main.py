import matplotlib.pyplot as plt

from analysis import StudentDataAnalyzer
from plotting import *

CSV_FILENAME = 'student_scores_random_names.csv'
EXCEL_FILENAME = 'average_scores_per_semester.xlsx'
SUBJECTS = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']

analyzer = StudentDataAnalyzer(CSV_FILENAME, SUBJECTS)
analyzer.clean_data()

failed_students = analyzer.get_failed_students()
average_semester_scores = analyzer.get_avg_semester_scores()
highest_avg_student = analyzer.get_highest_avg_student()
hardest_subject = analyzer.get_hardest_subject()
average_total_scores = analyzer.get_average_total_scores()


def write_to_excel(data):
    data.to_excel(EXCEL_FILENAME, index=False)


def display_statistics():
    print(f'Failed students list: {failed_students}')
    print('Average semester scores:')
    print(average_semester_scores)
    print(f'Student with highest average score: {highest_avg_student}')
    print(f'Hardest subject: {hardest_subject}')


def show_plots():
    plot_average_semester_scores(average_semester_scores)
    plt.figure()
    plot_average_total_scores(average_total_scores)


display_statistics()
write_to_excel(average_semester_scores.reset_index())
show_plots()
