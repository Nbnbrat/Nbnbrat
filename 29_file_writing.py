# file writing
#for every run rplace the existing text
f = open("bhoosh.txt","w")
f.write("bhooshan accha hai.")
f.close()

#for every run append  the existing text each time
# f = open("bhoosh1.txt","a")
# f.write("bhooshan accha hai.\nAnd smart bhi!")
# f.close()

#for counting d chacters in appended text
# f = open("bhoosh1.txt","a")
# a=f.write("bhooshan accha hai.\nAnd smart bhi!")
# print(a)
# f.close()

#handle both read and write
f = open("bhoosh.txt","r+")
print(f.read())
f.write("thank you")

f.close()