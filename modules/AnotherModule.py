#import entire module
# import myModule as module
#import specific function
from myModule import find_element_index as fei
courses = ['history', 'math', 'physics', 'compsci']
# print(module.test)
print(fei(courses, 'math'))