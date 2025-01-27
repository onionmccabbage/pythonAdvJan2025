# Args and Kwargs: positional arguments and keyword arguments

def usingArgs(*args): # the single asterisk gathers positional arguments into a tuple called 'args'
    '''for EVERY function in Python, any positional 
    arguments will ALWAYS be gathered into a tuple'''
    # iterate over the tuple, showing each positional memember
    print(type(args), args)
    for _ in args:
        print(f'Positional argument value is {_} is {type(_)}')

def usingKWArgs(**kwargs): # the double asterisk gathers all keyword arguments into a dict
    '''for EVERY function, any keyword arguments
    will ALWAYS be gathers into a dictionary'''
    print(type(kwargs), kwargs)
    # a Python dictionary is a non-ordinal collection of key-value pairs
    for (k,v) in kwargs.items():
        print(k, v)

def both(*args, **kwargs): # any keyword arguments must come AFTER any positional arguments
    print(args, kwargs)

# a practical use of this
def actDependantly(*args):
    '''this function acts differently according to the quantity of positional arguments'''
    if len(args)==0:
        return 'no args'
    elif len(args)==1:
        return args[0]
    elif len(args)==2:
        return args[0] + args[1]
    else:
        return args[len(args)-1] # return the last argument
    
if __name__ == '__main__':
    # call our functions
    # here we have arguments which are positional: 0, 1, 2, 3....
    usingArgs(4, 5, 6, True, [], (3,2,1), 'done')
    usingKWArgs(x=3, y=4, v=True, c=[6,5,4])
    both(4,3,2, x=99)
    print(actDependantly())
    print(actDependantly(1))
    print(actDependantly(1,2))
    print(actDependantly(1,2,3,4,5))
