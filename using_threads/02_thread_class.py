from threading import Thread
import time
import random

# we can tun cProfile against any module. It is designed for unit profiling, not for profiling imports
# at a command promt, type
# python -m cProfile -o prof_out 02_thread_class.py


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
        for _ in range(0,4):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*self.x)
            print(f'{self.n} no longer sleeping')

if __name__ == '__main__':
    print('on the main thread')
    tA = MyClass('A', .003)
    tB = MyClass('B', .003)
    tC = MyClass('C', .003)
    print('starting thread')
    tA.start()
    tB.start()
    tC.start()
    print('join the thread (main thread pauses until they join back)')
    tA.join()
    tB.join()
    tC.join()
    print('all done')