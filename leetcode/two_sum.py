def get_array_elements(a, number):
    dict = {}
    for i, element in enumerate(a):
        another_element = number-element
        if another_element in dict:
            print('pair found : ', (a[dict[another_element]], a[i]))
        else:
            dict[element] = i

print(get_array_elements([1,2,4,3,10,14],5))
# print(get_array_elements([3,3],6))