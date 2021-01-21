from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        print("comment: ", data)
        pos = self.getpos()
        print("\tAt Line: ", pos[0], "position ", pos[1])

def main():
    parser = MyHTMLParser()
    f= open("test.html")

    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)
main()