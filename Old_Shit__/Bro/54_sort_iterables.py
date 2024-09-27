# student = ("Squidward","Sady","Patrick","Spongbob","Krabs")

# # student.sort(reverse=False)
# sorted_s =sorted(student,reverse=True)

# for i in sorted_s:
#     print(i)

student = [
    ("Squidward", "F", 60),
    ("Sady", "A", 33),
    ("Patrick", "D", 36),
    ("Spongbob", "B", 20),
    ("Krabs", "C", 78)
]

student1 = (
    ("Squidward", "F", 60),
    ("Sady", "A", 33),
    ("Patrick", "D", 36),
    ("Spongbob", "B", 20),
    ("Krabs", "C", 78)
)
grade = lambda grades:grades[1]
age = lambda age:age[2]

student.sort(key=grade,reverse=False)
sorted_s = sorted(student1,key =age,reverse=False)

print(student)

for i in sorted_s:
    print(i)
