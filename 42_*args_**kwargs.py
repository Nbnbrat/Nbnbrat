# 3 type of arguments in function normal argument,*args,**kwargs
def arguments(normal,*argsnbn,**kwargsnbn):
    print(type(argsnbn))                            #type of arguments always in a tuple if its *argsnbn then itll give list type
    print(normal)
    print(argsnbn[0])
    for i in argsnbn:
         print(i)
    print('\nhere we are introducing the **kwargs arguments:')
    for key,values in kw.items():
        print(f'{key} is a {values}.')

kw = {'hari':'chef','mari':'gamer','shiva':'dancer'}
n = ['hari','mari','shiva']
nor = 'Iam normal argument and below is the *args elements:'
x = (arguments(nor,*n,**kw))                                                #we should call *args and **kwargs with prior *,** respectively
                                                                       # the passing arguments to a function should be in this order fun_name(normal,*args,**args)
                                                                       # *args and **kwargs are not mandatory we can call normal argument without passing the args and kwargs