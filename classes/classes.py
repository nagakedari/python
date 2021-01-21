class myTestClass():
    def __init__(self): #it acts like constructor
        print ("This is a constructor")
    def method1(self):
        print ("myTestClass method1")
    def method2(self, someString):
        print ("myTestClass method2 "+ someString)

# def main():
#     c = myTestClass()
#     c.method1()
#     c.method2("This is a test string")

# if __name__ == "__main__":
    # main()

#Inheritence
class myTestInheritanceClass(myTestClass):
    test_var=10
    def method1(self):
        myTestClass.method1(self)
        print ("myTestInheritanceClass method1")
    def method2(self, someString):
        print ("myTestInheritanceClass method2 "+ someString)

def main():
    c = myTestInheritanceClass()
    c.method1()
    c.method2("This is a test string")
    print(c.test_var);
    
if __name__ == "__main__":
    main()