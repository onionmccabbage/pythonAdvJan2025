

# this is a higher-order function, because it taks a function as an argument
def showArgs(f):
    '''reveal any arguments passed in to the function f'''
    def newFunc(*args, **kwargs):
        report = f'''Running a function called {f.__name__}
The positional arguments are: {args}
The keywprd arguments are {kwargs}'''
        print(report)
        return f(*args, **kwargs)
    return newFunc

# some simple functions we may wish to examine
@showArgs # the decorator will always act on the immediately-following function
def addThem(a,b):
    return a+b

@showArgs
def squareIt(a):
    '''return the square of a'''
    return a*a

@showArgs
def isOdd(w):
    '''return True if it is odd, Fasle otherwise'''
    return w%2 !=0

if __name__ == '__main__':
    r = addThem(4,5)
    s = addThem(a=2, b=6)
    t = addThem(2, b=9)
    w = squareIt(3) # 9
    o = isOdd(5) # True
