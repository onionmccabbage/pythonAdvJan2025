# simple print-to-file routine
def printTofile():
    '''use print to output to a persistent text file'''
    # NB better to use try-except here
    # this is a file access object
    fout = open('my_file.txt', 'at')
    # NB remember print ALWAYS defaults to adding a new line at the end
    print('the weather is normal', file=fout) # we redirect the default oprnt output to a file access object
    fout.close()

# slightly more nuanced write to file (using 'with')
def writeToFile(t='default'): # of arguments are optional, they are keyword arguments
    ''' use a file access object to write text to a file'''
    try:
        with open('my_file.txt', 'at') as fout: # 'with' will close the asset when no longer needed
            fout.write(t)
    except Exception as err:
        print(err)
# read from file
def readFromfile():
    '''read back from a text file'''
    # fin = open('my_file.txt', 'rt')
    # t = fin.read()
    # fin.close()
    # return t
    try:
        with open('my_file.txt', 'rt') as fin: # 'with' will close the asset when no longer needed
            t = fin.read()
        return t
    except Exception as err:
        print(err)

# bytes
def makeBytes(v): # potitional argument are NOT optional
    '''convert the string v into bytes'''
    b = bytes(v, 'UTF8') # or b = b'{v}'
    return b

# NB for truly optional arguments:
# write a method that expeects *args and/or **kwargs
# Se if tehre is anything in either collection and act accordingly

# write bytes
def writeBytesToFile(t):
    ''' use a file access object to write bytes to a file'''
    try:
        with open('my_file', 'ab') as fout: # 'with' will close the asset when no longer needed
            fout.write(t)
    except Exception as err:
        print(err)
# read bytes
def readBytesFromfile():
    '''read back from a byte file'''
    try:
        with open('my_file.txt', 'rb') as fin: # 'with' will close the asset when no longer needed
            t = fin.read()
        return t # we are return a byte object
    except Exception as err:
        print(err)

import json # this is part of the Python standard library

# JSON
def workWithJson():
    '''Here is a tuple of dictionaries'''
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )  
    # we may convert this structure to plain text
    j = json.dumps(creatures_t) # serialize the structure to text
    print(j, type(j))
    # We can also covert correctly-formatted JSON back into a structure
    s = json.loads(j)
    print(s, type(s)) # list


def seekContent(*args):
    '''if there is a number in the 'args' tuple ,then see to that position
    Otherwise return the whole file'''
    if len(args)==0:
        # there are no arguments passed in - return everything
        r = readFromfile()
        return r
    elif len(args)==1:
        try:
            with(open('my_file.txt', 'rt')) as fin:
                n = args[0]
                fin.seek(n)
                the_rest= fin.read()
            return the_rest
        except Exception as err:
            print(err)


if __name__ == '__main__':
    '''exercise the code'''
    # printTofile()
    # writeToFile('will the weather improve ?')
    # print( readFromfile() )
    writeBytesToFile( makeBytes('hello from text to bytes') )
    print(type(readBytesFromfile()))
    workWithJson()
    # call with no args
    s = seekContent() # expect everything
    print(s)
    print('---------------------')
    # call with one numberic arg
    r = seekContent(32)
    print(r)