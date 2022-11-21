# by using with block file will be closed no need to use close() function to close it
with open("bhoosh1.txt") as x:
    print(x.readline())
    a = x.readlines()
    print(a)
    print(x.readline())