# #Pattern
# #ask number of rows to print
# #take an binary number (0 or 1) with boolian if its true print acute triangle or print it reverse
# #print acute triangle pattern if
#
# row = int(input("enter no. of rows you want"))
# num = int(input("enter binary number 0 or 1"))
# new = bool(num)
# if new==True:
#     for i in range(1,row+1):
#         print()
#         for j in range(1,i+1):
#             print('*',end='')
# else:
#     for i in range(row,0,-1):
#         print()
#         for j in range(1,i+1):  #or for j in range(row):
#             print("*",end='')   #        print("*",end="")
#                                 #        row-=1


# try:
#     row = int(input("enter no. of rows you want"))
#     num = int(input("enter binary number 0 or 1"))
#     new=bool(num)
#
#     if new==True:
#         for i in range(1,row+1):
#             print('*'*i)
#     else:
#         for i in range(row,0,-1):
#             print('*'*i)
# except Exception as e:
#     print("invalid input")


row = int(input("enter no. of rows"))
num=bool(int(input("print 0 to get false")))

def pattern(row,num):
    if num==True:
        count = 1
        while count<=row:
            print(count*"*")
            count+=1
    else:
        count = row
        while count!=0:
            print(count*"*")
            count-=1


pattern(row,num)


