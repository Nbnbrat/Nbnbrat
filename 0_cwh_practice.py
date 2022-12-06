#1 take a list print duplicate elements
# l = [10,20,30,10,20,10]
# u = []
# d = []
# for i in range(len(l)):
#     if l[i] in u:
#         if l[i] not in d:
#             d.append(l[i])
#     else:
#         u.append(l[i])
# print(d)
# print(u)

#2 take an elements print duplicate elements
# l = [10,20,10,30,10,20]
#
# d = {}
# for i in range(len(l)):
#     if l[i] in d.keys():
#         count = d[l[i]]
#         d[l[i]] = count+1
#     else:
#         d[l[i]]=1

# for i,j in d.items():
#      # if j != 1:
#     #     print(i)
#     print(i,"is occuring",j,"times")

#3 given string n="((())" print true if open and close paranthesis are equal elsse print false
# n = '(()))'
# d={}
# for i in range(len(n)):
#     if n[i] in d.keys():
#         val = d[n[i]]
#         d[n[i]] = val+1
#     else:
#         d[n[i]] = 1
# if d["("] == d[")"]:
#     print("True")
# else:
#     print("False")

#4 take a list print 2nd largest number
# try:
#     l = [1, 1, 20, 25, 30, 25]
#     fbig = 0
#     sbig = 0
#     if len(l) == 0:
#         print('empty')
#
#     elif len(l) == 1:
#         print('no sbig')
#
#     if l[0] > l[1]:
#         fbig = l[0]
#         sbig = l[1]
#     else:
#         fbig = l[1]
#         sbig = l[0]
#
#     for i in range(2, len(l)):
#         if i in l == 0:
#             print('all the elements are zero')
#         elif l[i] > fbig:
#             sbig = fbig
#             fbig = l[i]
#         elif l[i] > sbig and fbig != l[i]:
#             sbig = l[i]
#         elif fbig == sbig:
#             sbig = l[i]
# except IndexError:
#     print('take more than 2 elements in a list')
#
# print(fbig)
# print(sbig)
# or
# l = [1,1,20,25,30,25]
# print('2nd largest number is', sorted(l)[-2])
# or
# l.sort()
# print('2nd largest number is', l[-2])

# print diamond pattern
#       *
#      ***
#     *****
#    *******
#     *****
#      ***
#       *
#
# n=4
# for i in range(n-1):
#     for j in range(i,n):
#         print('_', end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(i):
#         print('*', end=' ')
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print('_',end=' ')
#     for j in range(i,n):
#         print('*',end=' ')
#     for j in range(i,n-1):
#         print('*',end=' ')
#     print()

# butterfly
# n=4
# for i in range(n-1):
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(i,n-1):
#         print(' ',end=' ')
#     for j in range(i,n-1):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(i,n):
#         print('*',end=' ')
#     print()

# double hill
# n=3
# for i in range(n):
#     for j in range(i,n):
#         print('-',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i,n-1):
#         print('-',end=' ')
#     for j in range(i,n-1):
#         print('-',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()

# sandtime
# n=3
# for i in range(n-1):
#     for j in range(i+1):
#         print('-',end=' ')
#     for j in range(i,n):
#         print('*',end=' ')
#     for j in range(i,n-1):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print('-',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()

# right pascal triangle
# n=3
# for i in range(n-1):
#     for j in range(i,n):
#         print('-',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print('-',end=' ')
#     for j in range(i,n):
#         print('*',end=' ')
#     print()

# left pascals triangle
# n=3
# for i in range(n-1):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ')
#     print()

# no. of occurance with count for given word
# w = 'google'
# d = {}
# for i in range(len(w)):
#     if w[i] in d.keys():
#         val = d[w[i]]
#         d[w[i]] = val+1
#     else:
#         d[w[i]] = 1
#
# s = ''
# for i,j in d.items():
#     s = s+str(j)+str(i)+','
# print(s)

# print only adjacent pair of given word
# w = 'google'
# l = list(w)
# pos = 0
# while pos != len(l)-1:
#     if l[pos] == l[pos+1]:
#         l.pop(pos)
#         l.pop(pos)
#         if pos !=0:
#             pos = pos -1
#     else:
#         pos+=1
# s=''
# for i in l:
#    s = s+i
# print(s)
# prime number
num = int(input())
prime = True

# for i in range(2,(num//2)+1):
#     if num%i == 0:
#         print(num,'not prime')
#         prime = False
#         break
# if prime == True:
#     print(num,'is prime')





