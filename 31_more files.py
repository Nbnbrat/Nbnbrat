x=open("bhoosh1.txt")
#tell() function tells whre the file pointer is.
#print(x.tell())
print(x.readline())
#print(x.tell())
#seek() used for to reguide the pointer of the file it'll tell fro where to read the file
print(x.seek(0))
print(x.readline())
#print(x.tell())
x.close()