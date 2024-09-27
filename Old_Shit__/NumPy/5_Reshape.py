import numpy as np

a = np.arange(1,7)
print(a)
print(a.shape)

# b = a.reshape((3,2))
# print(b)
# print(b.shape)

b = a[:,np.newaxis]
print(b)
