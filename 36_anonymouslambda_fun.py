#anonymous or lambda function

# def add(a,b):
#     return a+b


# add = lambda x,y: x+y
#
# print(add(2,3))



a = [[14,6],[20,1],[3,3],[2,10]]
# def srt(a):
#     return a[1]
# a.sort(key=srt)      # here key is an argument which takes function as input
# print(a)

a.sort(key=lambda x:x[1])
print(a)