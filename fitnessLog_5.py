# Fitness log
# Create log for bhoosh,pavan and tippe for food and excercise
# and retrieve the data for the same whenever you want
import time
import clear
def timing():
    return time.asctime(time.localtime(time.time()))

def log(a):
    if b == 1:
        try:
            fx = int(input("Enter which data want to log? 1 for Food 2 for Exercise.\n"))
            if fx == 1:
                detail = input("Enter the detail about Bhoosh's food intake.")
                with open("bhooshfd.txt","a") as op:
                    op.write(f"{detail} on {timing()} \n")
                op.close()
                print("Food detail Logged successfully for Bhoosh.")
            elif fx == 2:
                detail = input("Enter the detail about Bhoosh's Excercise.")
                with open("bhooshex.txt","a") as op:
                    op.write(f"{detail} on {timing()} \n")
                    op.close()
                print("Exercise detail Logged successfully for Bhoosh.")
            else:
                print("Enter valid input")
        except ValueError:
            print("Enter either 1 or 2")

    elif b == 2:
        try:
            fx = int(input("Enter which data want to log? 1 for Food 2 for Exercise.\n"))
            if fx == 1:
                detail = input("Enter the detail about Pavan's food intake.")
                with open("pavanfd.txt", "a") as op:
                    op.write(f"{detail} on {timing()} \n")
                op.close()
                print("Food detail Logged successfully for Pavan.")
            elif fx == 2:
                detail = input("Enter the detail about Pavan's Excercise.")
                with open("pavanex.txt", "a") as op:
                    op.write(f"{detail} on {timing()} \n")
                    op.close()
                print("Exercise detail Logged successfully for Pavan.")
            else:
                print("Enter valid input")
        except ValueError:
            print("Enter either 1 or 2")

    elif b == 3:
        try:
            fx = int(input("Enter which data want to log? 1 for Food 2 for Exercise.\n"))
            if fx == 1:
                detail = input("Enter the detail about Tippe's food intake.")
                with open("tippefd.txt", "a") as op:
                    op.write(f"{detail} on {timing()} \n")
                op.close()
                print("Food detail Logged successfully for Tippe.")
            elif fx == 2:
                detail = input("Enter the detail about Tippe's Excercise.\n")
                with open("tippeex.txt", "a") as op:
                    op.write(f"{detail} on {timing()} \n")
                    op.close()
                print("Exercise detail Logged successfully for Tippe.")
            else:
                print("Enter valid input")
        except ValueError:
            print("Enter either 1 or 2")

def retrieve(a):
    if b == 1:
        try:
            fx = int(input("Enter 1 to view food intake details 2 for Exercise details of Bhoosh."))
            if fx == 1:
                with open("bhooshfd.txt") as op:
                    for i in op:
                        print(i)
                    #print(op.readlines())
                op.close()
            elif fx == 2:
                with open("bhooshex.txt") as op:
                    for i in op:
                        print(i)
                    #print(op.readlines())
                op.close()
            else:
                print("Enter valid input")
        except ValueError:
            print("Enter either 1 or 2")

    elif b == 2:
        try:
            fx = int(input("Enter 1 to view food intake details 2 for Exercise details of Pavan."))
            if fx == 1:
                with open("pavanfd.txt") as op:
                    for i in op:
                        print(i)
                    #print(op.readlines())
                op.close()
            elif fx == 2:
                with open("pavanex.txt") as op:
                    for i in op:
                        print(i)
                    #print(op.readlines())
                op.close()
            else:
                print("Enter valid input")
        except ValueError:
            print("Enter either 1 or 2")

    elif b == 3:
        try:
            fx = int(input("Enter 1 to view food intake details 2 for Exercise details of Tippe."))
            if fx == 1:
                with open("tippefd.txt") as op:
                    for i in op:
                        print(i)
                    #print(op.readlines())
                op.close()
            elif fx == 2:
                with open("tippeex.txt") as op:
                    for i in op:
                        print(i)
                    #print(op.readlines())
                op.close()
            else:
                print("Enter valid input")
        except ValueError:
            print("Enter either 1 or 2")


resume = True
while resume:
    print("--------Welcome To The Fitness Log!--------")
    a = int(input("Enter 1 for Log the detail and 2 for retrieve the details.\n"))
    if a == 1:
        b = int(input("Enter 1 for Bhoosh, 2 for Pavan,and 3 for Tippe.\n"))
        log(a)
    elif a == 2:
        b = int(input("Enter 1 for Bhoosh, 2 for Pavan,and 3 for Tippe.\n"))
        retrieve(a)
    else:
        print("Please Enter valid input")

    print()
    relog = input("Do you wanna relog or retrieve log data again? Type y for yes, n for no.\n")
    if relog == "y":
        resume = True
    else:
        resume = False
