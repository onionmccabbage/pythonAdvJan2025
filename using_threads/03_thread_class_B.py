from threading import Thread
import time
import random

class SimpleClass(): # this class does NOT inherit from 'thread'
    def __init__(self):
        pass
    def __call__(self, n):
        '''the __call__ function lets us invoke this class on a thread'''
        msg = ''
        for _ in range(0,4):
            msg += f'{n} is sleeping'
            time.sleep(random.random()*0.2)
        print(msg)

def main():
    thread_list = []
    cA = SimpleClass()
    for _ in range(0,8):
        '''append each new thread to a list of threads'''
        thread_list.append( Thread(target=cA, args=(_,)) )
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()

if __name__ =='__main__':
    main()