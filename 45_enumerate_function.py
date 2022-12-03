l = ['pen','chocolate','candy','milk']

# i=0
# for item in l:
#     if i%2 is not 0:
#         print(f'jarvis please bring {item}.')
#     i+=1

for i,item in enumerate(l):
    if i%2 is not 0:
        print(f'jarvis please bring {item}')


# enumerate function gives access to both index number and items in a variable