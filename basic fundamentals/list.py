persons = ["srini", "naga", "vasu", "kedari"]

#length
# print(len(persons))

# #last index value
# print(persons[-1])

# #range of values (upper limit not inclusive)
# print(persons[0:3])

# #range of values starting from one index to all values
# print(persons[2:])

# #append
# persons.append("nagakedari")
# print(persons)

#insert at specific localtion
# persons.insert(1, "vasukedari")
# print(persons)
# #To insert a list inside a list [[val1, val2], val3, val4]
# persons1 = ["aarush", "akedari"]
# persons.insert(0, persons1)
# print(persons)
# # #to add a list into another list as individual elements rather than a list inside a list [val1, val2, val3, val4] val1 and val2 are added from anothe list
# persons.extend(persons1)
# print(persons)
# # #remove a value from list
# persons.remove(["aarush", "akedari"])
# print(persons)
# stackpointer = persons.pop()
# print(stackpointer)
# print(persons)
# # #sort list
# persons.reverse()
# print(persons)
# persons.sort()
# print(persons)
# persons.sort(reverse=True)
# print(persons)
# #join list elements with delimiter
# joinedString = ','.join(persons)
# print(joinedString)
# #list are mutable

# list_1 = ['history', 'math', 'physics', 'compsci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1.append('telugu')

# print(list_1)
# print(list_2)

# #creating empty list
# empty_list = []
# #or
# empty_list = list()

# test_list = list()
# tail = -1
# test_list.append(2)
# tail += 1
# test_list.append(3)
# tail += 1
# test_list.append(4)
# tail += 1
# test_list.append(5)
# tail += 1
# test_list.append(6)
# tail += 1
# test_list.append(7)
# tail += 1
# print(test_list)
# print(test_list[0])
# print(test_list[tail])
# del test_list[0]
# print(test_list)
# print(test_list[0])
# print(tail)
# print(test_list[tail])