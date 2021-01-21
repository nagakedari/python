def binary_search(array, min, max, value):
    if min > max:
        return -1
    mid = int((min+max) / 2)
    if value == array[mid]:
        return mid
    elif value < array[mid]:
        return binary_search(array,min,mid-1, value)
    else:
        return binary_search(array, mid+1, max, value)   
        
        
array = [1,3,5,7,8,9,10,15,16]
print(binary_search(array, 0, len(array)-1, 15))
print(binary_search(array, 0, len(array)-1, 16))
print(binary_search(array, 0, len(array)-1, 8))
print(binary_search(array, 0, len(array)-1, 1))
print(binary_search(array, 0, len(array)-1, 3))
print(binary_search(array, 0, len(array)-1, 25))
print(binary_search(array, 0, len(array)-1, 0))