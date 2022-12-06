# using __name__ __main__
def addstr(str):
    return f'This function is working fine {str}.'

def wrongadd(a,b):
    print("this fun do wrong sum of 2 numbers")
    return a+b+5

print('this module function name is',__name__)

if __name__ == '__main__':                         #this __name__ main fun defined here means the name is __main__for this file
    print(addstr('bhooshan'))                     # only here itwill execute this print statements not in other file if we import this file as a module
    s = wrongadd(5,3)
    print(s)