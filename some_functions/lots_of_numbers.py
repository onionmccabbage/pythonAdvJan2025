from util import squareIt
from util import isOdd

def main():
    '''this is a common way to gather 'main' functionality'''
    # a large data set
    big = range(0, 10001) # (start, stop-before, step=1)
    # both map and filter objects are iterable results
    results_list = [i for i in map(squareIt, big)] # or separate into several lines
    print(results_list)
    odds_list = [i for i in filter(isOdd, big)]
    print(odds_list)
    print('done')

if __name__ == '__main__':
    main()