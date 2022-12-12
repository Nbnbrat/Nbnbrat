#  DECORATER

def dec_sq_qb(num):
    def sq_num_qb():
        sq= a**2
        print(f'The square of the number is: {sq}')
        num()
        qb = a**3
        print(f'The cube of the number is: {qb}')
    return sq_num_qb

a = int(input("Enter the number "))

@dec_sq_qb
def number():
    print(f'The number you choosed is: {a}')

# number = dec_sq_qb(number)

number()

def dec1(fun):
    def fun2():
        print('Head decorated')
        fun()
        print('Bottom decorated')
    return fun2
@dec1
def body():
    print('im naked!')

# body = dec1(body)

body()


