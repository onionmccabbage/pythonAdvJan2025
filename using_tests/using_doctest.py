import doctest

def cubeIt(a):
    '''return the cube of a
    >>> cubeIt(2)
    8
    '''
    return a**3

if __name__ == "__main__":
    c = cubeIt(3)
    print(c)
    # invoke doctest
    doctest.testmod(verbose=True)