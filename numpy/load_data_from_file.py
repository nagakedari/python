import numpy as np
import os

current_path = os.path.dirname(__file__)
filedata = np.genfromtxt(os.path.join(current_path, 'data.txt'), delimiter=",")
filedata = filedata.astype('int32')
print(filedata)

#####Boolean Masking and advanced Indexing #######

#indexing with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,5]])

print(filedata>50 )
print(filedata[filedata >50])
print(np.any(filedata > 50, axis=1))
#multiple conditions
print(((filedata >50) & (filedata <90)))
#not equal
print(~((filedata >50) & (filedata <90)))

a = np.array([[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25],
            [26,27,28,29,30]])
print(a[2:4, 0:2])
print(a[[0,1,2,3], [1,2,3,4]])

print(a[0:-2, 0:-2])
print(a[[0,4,5], 3:])