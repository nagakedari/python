def custom_decorator(func):
    def func_wrapper():
        print("execute pre function")
        func()
        print("execute post function")
    return func_wrapper

@custom_decorator
def question():
    print("Can you give me a discount on thay?")


question()
