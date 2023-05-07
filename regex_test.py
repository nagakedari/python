import re, array

pattern = re.compile('loss= ([0-9\\.]+)')

print(pattern.search('loss: 0.3293'))

a = array.array('f', [1,4,7,2,0,9,2.3])

print(a[::-1])

def traingle(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1)) 
traingle(9)