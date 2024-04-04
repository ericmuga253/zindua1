students = {
    'Alice': [85, 90, 92],
    'Bob': [78, 82, 80],
    'Charlie': [95, 89, 92],
    'David': [70, 75, 72]
}

# Average grades per student:
average_grades = {
    student: sum(grades) / len(grades) for student, grades in students.items()
    }

print(average_grades)

# determine which student has the highest average grade by using the max function with a key argument 

 '''student_with_highest_average = max(average_grades, key=average_grades.get) 
highest_average_grade = average_grades[
fwv-mscy-hsh'''