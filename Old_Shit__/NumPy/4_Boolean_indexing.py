import numpy as np

a= np.array([[1,2],[3,4],[5,6]])

# print(a)

bool_index = a>2
# print(bool_index)

# print(a[bool_index])

# print(a[a>2])

# b = np.where(a>2,a,"FUCK")
# print(b)

a = np.array([10,19,30,41,50,61])
# print(a)

# print(a[[1,3,5]])
even = np.argwhere(a%2==0).flatten()
print(a[even])
