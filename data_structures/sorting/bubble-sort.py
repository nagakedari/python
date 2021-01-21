def bubble_sort(array):
    i = 0
    while i < (len(array) -1):
        j = i+1
        while j <len(array):
            if(array[i]>array[j]):
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
            j+=1
        i+=1
    return array

print('Sorted array: {}'.format(bubble_sort([2,4,7,1,9,5,6])))