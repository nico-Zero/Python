employee_file = open("/media/nonesuch/Software/__/Python/employees.txt", "r")

for p in employee_file.readlines():
    print(p)

print("\n")
print(employee_file.read())
print("\n")


employee_file.close()

with open("/media/nonesuch/Software/__/Python/employees.txt", "r") as x:
    print(x.read())
 