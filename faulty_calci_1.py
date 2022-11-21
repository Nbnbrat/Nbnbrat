
# Faulty Calculator #

def calci():
    op = input("enter math operation choosing any one given :*,/,-,+")
    n1 = int(input("enter num1:"))
    n2 = int(input("enter num2:"))
    new = str(n1)+op+str(n2)

    if new=="45*5":
        print(777)
    elif new=="50+2":
        print(77)
    elif new=="42/5":
        print(7)
    elif op=="*":
        print(n1*n2)
    elif op=="+":
        print(n1+n2)
    elif op=="-":
        print(n1-n2)
    elif op=="/":
        print(n1/n2)
    else:
        print("Error! check your input")

    again()

def again():
    cal_again=input("Do you want to calculate again? if yes type 'y' or type 'n' for no.").lower()
    if cal_again=='y':
        calci()
    elif cal_again=='n':
        print("thank you see you again!")
    else:
        again()

calci()



