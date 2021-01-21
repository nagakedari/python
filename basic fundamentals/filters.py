grades = ['A', 'B', 'C', 'F', 'A', 'F']

def remove_fails(grade):
    return grade != 'F'

print(list(filter(remove_fails, grades)))

# Other ways to filter 

# using for loop
filtered_grades = []
for grade in grades:
    if grade != 'F':
        filtered_grades.append(grade)

print(filtered_grades)

#using comprehension

print([grade for grade in grades if grade != 'F'])