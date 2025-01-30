import threading

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
    while counter <10:
        counter += 1
        print(f'Worker A sets count to {counter}')

def workerB():
    ''' this worker will access the global xcounter and decrement by one'''
    global counter
    while counter >-10:
        counter -= 1
        print(f'Worker B sets count to {counter}')


if __name__ == '__main__':
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t1.start()
    t2.start()
    t1.join()
    t2.join()