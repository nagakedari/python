#basic function
def basicFunc():
    print("I am a function")

basicFunc()
print(basicFunc())
print(basicFunc)

# Function with argument
def argumentsFunc(arg1, arg2):
    print(arg1, " ", arg2)

def cubeFunc(x):
    return x*x*x

argumentsFunc(10, 20)
print(argumentsFunc(10,20))
print(cubeFunc(2))

#Default argument value
def power (num, x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result

print(power(2))
print(power(2, 3))
print(power(x=3, num=2))

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(8,4,5,8,5))