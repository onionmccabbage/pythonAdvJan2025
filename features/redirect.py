import sys

class RedirectOut():
    '''redirect the standard output to a different stream,
    When done, set the standard output back to what it was'''
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout
    # __enter__ is used every time an instance is invoked
    def __enter__(self):
        self.original_stdout = sys.stdout
        sys.stdout = self.new_stdout
    # __exit__ is used every time an instance finished being invoked
    def __exit__(self,  exc_type, exc_value, exc_traceback): # NB all these must be present
        sys.stdout = self.original_stdout


if __name__ == "__main__":
    print(sys.stdout, sys.stdin, sys.stderr)
    with open('my_log.txt', 'a') as fobj:
        r = RedirectOut(fobj) # an instance of our class object
        with r:
            print('this ends up in a log file')
    # NB when 'with' block ends, it will automatically close the resource
    print('normal service resumed')