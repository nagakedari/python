#for loop
def main():
    for x in range(5, 10):
        print(x)

main()

#loop over collection
# def main1():
#     days = ["Mon", "Tue", "Wed"]
#     for x in days:
#         print(x)

# main1()

# using enumerate()
def main2():
    days = ["Mon", "Tue", "Wed"]
    for i, x in enumerate(days): #enumerate returns index and the value
        print(i, x)

main2()
