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

# read from file

# bytes

# JSON


if __name__ == '__main__':
    '''exercise the code'''
    printTofile()