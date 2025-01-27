# a pure function has no side effects. For any given input(s) the outcome is entirely deterministic
# we may also write impure functions, where the outcome cannot be predicted


def squareIt(a):
    '''return the square of a'''
    return a*a

def isOdd(w):
    '''return True if it is odd, Fasle otherwise'''
    return w%2 !=0

def addThem(m,n ):
    return m+n