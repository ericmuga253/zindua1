students={
    'john':[88,90,86],
    'kate':[86,78,94],
    'jane':[80,84,90],
    'tim':[88,98,96]
}
average_grade={}
for student, scores in students.items():
    average_grade[student]=sum(scores)/len(scores)


    