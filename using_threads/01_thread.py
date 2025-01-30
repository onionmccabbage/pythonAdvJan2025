from threading import Thread
import time

def fn(n):
    '''this is a normal function just like any other'''
    time.sleep( 1 )
    print(f'This is function {n}')

if __name__ == '__main__':
    #we could invoke the function procedurally (in the normal way)
    # fn('A')
    # fn('B')
    # fn('C')
    # we try to control threads through the Thread class
    # threads are ultimately managesby the operating system
    tA = Thread(target=fn, args=('A',)) # a one-member tuple
    tB = Thread(target=fn, args=('B',))
    tC = Thread(target=fn, args=('C',))
    print('on the main thread')
    tA.start() # the threads will begin in the order they are started
    tB.start()
    tC.start()
    # by default, running additional threads does not block the main thread
    # it is common to use 'join' so tje main thread waits for the other threads to complete
    tB.join()
    tA.join()
    tC.join()
    print('all done')