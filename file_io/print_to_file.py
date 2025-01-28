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
def writeToFile(t):
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
def makeBytes(v):
    '''convert the string v into bytes'''
    b = bytes(v) # or b = b'{v}'
    return b

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


# JSON


if __name__ == '__main__':
    '''exercise the code'''
    # printTofile()
    # writeToFile('will the weather improve ?')
    # print( readFromfile() )
    writeBytesToFile( makeBytes('hello from text to bytes') )
    print(type(readBytesFromfile()))