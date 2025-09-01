def calculate_homework(homework_assigment_grades):
    sum_of_grades = 0
    for homework in homework_assigment_grades.values():
        sum_of_grades += homework

    final_grade = round(sum_of_grades / len(homework_assigment_grades), 2)
    print(final_grade)
