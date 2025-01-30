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