# map function
# l = ['2','3','4']
# l = list(map(int,l))
# print(l)

# def m1(a):
#     return a*a
#
# num = [2,3,5]
# l = tuple(map(m1,num))
# print(l)

# l = list(map(lambda x:x*x,num))
# print(l)


# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# fun = [square,cube]
# for i in range(5):
#     l=list(map(lambda x:x(i),fun))
#     print(l)

# ------------------------------------------FILTER---------------------
# l = [2,4,5,1,6,48,-50,8]
# def grt_5(n):
#    return n>5
#
# grt_5_lst = list(filter(grt_5,l))

# using lambda
# grt_5_lst = list(filter(lambda x:x>5,l))
# print(grt_5_lst)
#------------------------------------------------REDUCE------------------
l=[1,2,3,4,5,8]
# total=0
# for i in l:
#     total+=i
# print(total)
from functools import reduce
l = reduce(lambda x,y:x+y,l)
print(l)
