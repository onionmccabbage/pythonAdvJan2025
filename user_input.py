# Very often there is NO user sat watchniog our running code
# EVERY user input is ALWAYS a string (never anything else)

def askUser():
    '''Invite the user to enter a positive integer'''
    while True:
        n = input('Please enter a positive integer: ')
        # NB we could try using 'isnumeric' for digits=only checking
        try:
            v = abs(int(float(n)))
            return v
        except Exception as err:
            pass
        # we could also use 'break'
    

if __name__ == '__main__':
    p = askUser()
    print(p, type(p))
