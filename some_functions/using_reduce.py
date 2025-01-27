# reduce is part of the Python standard library, in 'functools'
import functools
# from functools import reduce
import util # we have all the utility functions

if __name__ == '__main__':
    # some data
    d = range(0, 11)

    # apply map to this data
    d_sq = map(util.squareIt, d) # we have a map object

    # find the cumulative results of all the data
    total = functools.reduce(util.addThem, d_sq)
    print(total)
