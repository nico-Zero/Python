student_score = input("Input the heights of the students : ").split(',')
student = (int(i) for i in student_score)
highest_score = max(student)
print(f"The Highest score is {highest_score}.")
