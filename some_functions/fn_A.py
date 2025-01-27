# Args and Kwargs: positional arguments and keyword arguments

def usingArgs(*args): # the single asterisk gathers positional arguments into a tuple called 'args'
    '''for EVERY function in Python, any positional 
    arguments will ALWAYS be gathered into a tuple'''
    # iterate over the tuple, showing each positional memember
    print(type(args), args)
    for _ in args:
        print(f'Positional argument value is {_} is {type(_)}')


if __name__ == '__main__':
    # call our functions
    # here we have arguments which are positional: 0, 1, 2, 3....
    usingArgs(4, 5, 6, True, [], (3,2,1), 'done')