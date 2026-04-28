student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for key in student_scores:
    if student_scores[key] >= 91:
        print(f"{key} Outstanding grade!: {student_scores[key]}%")
    elif student_scores[key] <= 90 and student_scores[key] >= 81:
        print(f"{key} Exceeds Expectations!: {student_scores[key]}%")
    elif student_scores[key] <= 80 and student_scores[key] >= 71:
        print(f"{key} Acceptable: {student_scores[key]}%")
    else:
        print(f"{key} Fail: {student_scores[key]}%") 