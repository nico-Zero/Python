from numpy import square


student = list(range(100,-1,-10))
print(student)

square = [i * i for i in student]
print(square)

passed = [x for x in student if x >= 60 ] 
print(passed)

failed = [x if x < 60 else 'Passed'for x in student] 
print(failed)
