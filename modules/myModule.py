print('My Module got imported.........')

test = "Test string........."

def find_element_index(element_list, element):
    for i, value in enumerate(element_list):
        if value == element:
            return i
    return -1