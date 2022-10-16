student_scores = {
    "Harry": 81,
    "Ron": 79,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
for key,dict in student_scores.items():
    if 91<dict<100:
        student_scores[key] = "Outstanding"
    elif 81<dict<90:
        student_scores[key] = "Exceed Expectations"
    elif 71<dict<80:
        student_scores[key] = "Acceptable"
    else:
        student_scores[key] = "Fail"

print(student_scores)
