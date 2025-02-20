def fun(*args,**kwargs):
    prin('positional args: ',args)
    print('keyword args: ',kwargs)
    print(type(args))
fun(5,2,a=3,b=4)
