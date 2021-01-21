import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(np.min(a))
print(np.min(a, axis=1))
print(np.max(a, axis=1))
print(np.sum(a, axis=1))