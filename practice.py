students = {
    'John':[88,90,86],
    'Kate':[86,78,94],
    'Jane':[80,84,90],
    'Tim':[88,98,96]
}
average_grades = {}
for student, scores in students.items():
    average_grades[student] = sum(scores) / len(scores)
for student, average_grade in average_grades.items():
    print(f"{student}'s average grade: {average_grade:.2f}")
highest_average_student = max(average_grades, key=average_grades.get)
highest_average_grade = average_grades[highest_average_student]
print(f"{highest_average_student} has the highest average grade: {highest_average_grade:.2f}")
threshold = 85
print(f"Students with average grade above {threshold}:")
for student, average_grade in average_grades.items():
    if average_grade > threshold:
        print(student)