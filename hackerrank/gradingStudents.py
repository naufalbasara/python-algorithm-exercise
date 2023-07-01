def gradingStudents(grades):
    newGrades = []

    for grade in grades:
        if grade < 38:
            newGrades.append(grade)
        elif grade%5 >= 3:
            grade = grade+(abs((grade%5)-5))
            newGrades.append(grade)
        else:
            newGrades.append(grade)
    return newGrades

grades = [89, 28, 19, 10]
print(gradingStudents(grades))