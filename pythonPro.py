def fun(*args,**kwargs):
    print('positional args: ',args)
    print('keyword args: ',kwargs)
    print(type(args))
fun(1,2,a=3,b=4)
