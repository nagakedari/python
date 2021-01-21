nums = [1,2,3,4,5,6]

def square(i):
    return i*i

print(list(map(square, nums)))

#using lambda

print(list(map(lambda i: i*i, nums)))