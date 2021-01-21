import numpy as np

a = np.array([1,2,3])
a = a+4
print(a)
a= a-2
print(a)
a= a*2
print(a)
a= a/2
print(a)
a = np.array([1,2,3])
b = np.array([[2,3,4], [5,6,7]])
print(a+b)
print(a*b)
print(np.sin(a))
print(np.cos(a))

#########LINEAR ALGEBRA############
a  = np.ones((2,3))
b = np.full((3,2), 2)
print(np.matmul(a,b))

c = np.identity(3)
print(np.linalg.det(c))

#https://docs.scipy.org/doc/numpy/reference/routines.linalg.html