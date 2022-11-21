x=89
def har():
    x=20
    def bar():
        global x # global keyword by using this it will change the global variable value and search x in out of function
        x = 77
    print(x)
    bar()
    print("i",x)
har()
print(x)
