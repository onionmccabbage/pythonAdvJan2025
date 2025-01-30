from threading import Thread
import time
import random

# he best way to time code execution is the timeit library
import timeit

class SimpleClass(): # this class does NOT inherit from 'thread'
    def __init__(self):
        pass
    def __call__(self, n):
        '''the __call__ function lets us invoke this class on a thread'''
        msg = ''
        for _ in range(0,4):
            msg += f'{n} is sleeping'
            time.sleep(random.random()*0.5)
        # try to avoid printing from a thread (or anything i/o bound)
        # print(msg)

def main():
    start = timeit.default_timer()
    thread_list = []
    cA = SimpleClass()
    for _ in range(0,16):
        '''append each new thread to a list of threads'''
        thread_list.append( Thread(target=cA, args=(_,)) )
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()
    end = timeit.default_timer()
    print(f'Total execustion {end-start}')

if __name__ =='__main__':
    main()