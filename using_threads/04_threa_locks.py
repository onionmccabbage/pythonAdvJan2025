import threading
import timeit
# All Python threads share the same resources
# there will be obly one copy of python
# each thread is give its own heap
# this means threads cannot acess each others data (heap)
# There may be issues accessing global data

counter = 0
lock = threading.Lock()

def workerA():
    ''' this worker will access the global xcounter and increment by one'''
    global counter
    i = [] # this is NOT shared, so the lock ignores it
    lock.acquire() # get exclusive access to any shared assets
    while counter <10:
        counter += 1
        i.append(counter)
        print(f'Worker A sets count to {counter}')
    print(i)
    lock.release()

def workerB():
    ''' this worker will access the global xcounter and decrement by one'''
    global counter
    lock.acquire()
    while counter >-10:
        counter -= 1
        print(f'Worker B sets count to {counter}')
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    
    start = timeit.default_timer()
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print(f'main thread coninues {counter}')
    end = timeit.default_timer()
    print(f'{end-start}')