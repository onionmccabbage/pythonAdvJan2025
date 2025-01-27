# as well as class-based progams, we may write function-based programs
# map lets us apply a function acroos a collection of values
from util import squareIt
from util import isOdd

if __name__ == '__main__':
    # we need some data 
    d = (4,6,2,8,9,2,6)
    e = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4]
    # using map
    squares = map(squareIt, d)
    print(squares)
    # we then iterate over the map object to see any results
    print( squares.__next__() ) # 16
    print('..............')
    for r in squares:
        print(r)
    # using filter
    odds = filter(isOdd, e)
    print(odds) # we have a filter object
    odd_nums = [i for i in odds] # a quick way to et members of an iterable
    print(odd_nums)
