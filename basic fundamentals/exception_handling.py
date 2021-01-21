class MyException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

def main():
    try:
        f = open("./testtextfile.txt")
        if f.name == "testtextfile.txt":
            raise MyException('Raising My own exception')
    except FileNotFoundError as e:
        print('sorry! File Doesn\'t exists', e)
    except MyException as mye:
        print("MyException has been raised and caught ", mye)
    except Exception as e:
        print('Exception happend while reading the file', e)
    else:
        #code gets executed if we dont get an error in try block
        print(f.read())
        f.close()
    finally:
        print("Printing in Finally Block........")
main()