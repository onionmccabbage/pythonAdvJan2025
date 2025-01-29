# omprehension means dealing with every member of a collection, comprehensively
# here, the generstor will yield each succesive value as it is requested
# NB the values do NOT persist in memory, they are yielded on demand
my_generator = (i*i for i in range(0,10)) # this is NOT a tuple
my_l = [i*i for i in range(0,10)] # a list - all the values exist in memory

print(type(my_generator), type(my_l))

print(my_generator.__next__()) # 0
print(my_generator.__next__()) # 1
print(my_generator.__next__()) # 4
print('---------------------')
for _ in my_generator:
    print(_)
# this next line should fail - the generator has been exhausted
# print(my_generator.__next__()) # StopIteration exception

# we may choose to write our own custom generator
import datetime
import time


def genTimestamp():
    '''Custom generators are simply normal function
    The difference is we use 'yield' instead of 'return' '''
    while True: # endless loop
        t = datetime.datetime.now().strftime("%H:%M:%S")
        yield t

if __name__ == '__main__':
    # in order to make use of a generator we must create an instance of it
    ts_gen = genTimestamp() # an instance of a function (not a class)
    for _ in range(0,10):
        time.sleep(2.5)
        ts = ts_gen.__next__() # in order to call __next__() we must be working with a generator (yield)
        print(f'The time is {ts}')

