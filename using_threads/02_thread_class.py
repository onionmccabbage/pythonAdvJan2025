from threading import Thread
import time
import random

class MyClass(Thread): # our class inherits everything from the Thread class
    '''Any clas my inherit from Thread'''
    def __init__(self, n, x):
        # for Threads, it is often tidier t ocall Thread.__init__() rsthe than super().__init__
        # super().__init__(group, target, name, args, kwargs, daemon=daemon)
        Thread.__init__(self)
        self.n = n
        self.x = x
    # we override the 'run' ,ethod of the thread class
    def run(self):
        ''' When this thass is invoked the following code will run on a new thread'''
        print(f'{self.n} is sleeping')
        time.sleep(random.random()*3)
        print(f'{self.n} no longer sleeping')

if __name__ == '__main__':
    print('on the main thread')
    tA = MyClass('A', 3)
    tB = MyClass('B', 3)
    tC = MyClass('C', 3)
    print('starting thread')
    tA.start()
    tB.start()
    tC.start()
    print('join the thread (main thread pauses until they join back)')
    tA.join()
    tB.join()
    tC.join()
    print('all done')