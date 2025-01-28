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
    fin = open('my_text.txt', 'rt')
    t = fin.read()
    fin.close()
    return t

# bytes

# JSON


if __name__ == '__main__':
    '''exercise the code'''
    # printTofile()
    # writeToFile('will the weather improve ?')
    print( readFromfile() )