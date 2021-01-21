# print("Hello World")

# f=1
# print(f)

# f="abc"
# print(f)

print("This is a string" + str(123))
f=23
def someFunction():
    f= "wer"
    print(f)
someFunction()
print(f)

#To effect the global variable inside function

v=23
def someFunction1():
    global v
    v= "wer"
    print(v)
someFunction1()
print(v)
del v
print(v)