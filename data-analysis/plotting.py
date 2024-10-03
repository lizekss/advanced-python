from matplotlib import pyplot as plt


def plot_average_semester_scores(data):
    data.plot(kind='bar', figsize=(10, 7))
    plt.title('Average Scores by Subject for All Semesters')
    plt.xlabel('Semester')
    plt.ylabel('Average Score')
    plt.legend(title='Subjects', loc='upper left')


def plot_average_total_scores(data):
    data.plot(kind='line', figsize=(10, 7), marker='o')
    plt.title('Average Total Score per Semester')
    plt.xlabel('Semester')
    plt.ylabel('Average Total Score')
    plt.grid(True)
    plt.show()
