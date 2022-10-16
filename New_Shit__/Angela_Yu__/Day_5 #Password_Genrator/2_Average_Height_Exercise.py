student_height = input("Input the heights of the students : ").split(',')
student = (int(i) for i in student_height)
average =  sum(student)/len(student_height)

print(f"Average of the students height is {round(average)}.")
