import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape(2,2, 2)
print(after)

#vertical stacking matrices
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2]))

#horrizontal stacking matrices
h1 = np.array([1,2,3,4])
h2 = np.array([5,6,7,8])
print(np.hstack([v1,v2]))

