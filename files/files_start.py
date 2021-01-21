import os
from os import path
import datetime
from datetime import time
import time
def main():
    f= open("testtextfile.txt", "w+")
    f= open("testtextfile.txt", "a") # to append data to an existing file content instead of overriding
    for i in range(10):
        f.write("This is line "+ str(i)+"\r\n")
    f.close()
    # read whole file
    f= open("testtextfile.txt", "r")
    if f.mode == 'r':
        content = f.read()
        print(content)
    
    #Read line by line
    f= open("testtextfile.txt", "r")
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)
    
    #Path utils
    print(os.name)

    print("Item exists: "+str(path.exists("testtextfile.txt")))
    print("Item is a file: "+str(path.isfile("testtextfile.txt")))
    print("Item is a directory: "+str(path.isdir("testtextfile.txt")))
    print("Item path: "+str(path.realpath("testtextfile.txt")))
    print("Item path and Name: "+str(path.split(path.realpath("testtextfile.txt"))))

    t= time.ctime(path.getmtime("testtextfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("testtextfile.txt")))

    
main()