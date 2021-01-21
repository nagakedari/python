def main():
    x,y = 20,100

    if( x< y):
        st= "x is less than y"
    elif (x==y ):
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    print(st)
    st= "x is less than y or equal to y" if (x<=y) else "x is greater than y"
    print(st)
main()