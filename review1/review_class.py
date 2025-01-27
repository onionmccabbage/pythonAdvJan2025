from my_abc import ABCReview

class NumberFun(): # no special inheritance
# class NumberFun(ABCReview):
    __slots__ = ('__n',) # these slots need to be in the highest hierachy
    def __init__(self, num):
        self.n = num # use the setter method
    def __str__(self):
        return f'''The {self.findEvenOdd()} number {self.n} squared is {self.findSquare()}
and the square root of {self.n} is {self.findSqrt()}
It is {self.findIfSquareNum()}''' # use the accessors
    def findSquare(self):
        return self.__n ** 2
    def findSqrt(self):
        return self.__n ** 0.5
    def findEvenOdd(self):
        return 'even' if self.n%2 == 0 else 'odd'
    def findIfSquareNum(self):
        r = self.findSqrt()
        if r==int(r):
            return 'a square number'
        else:
            return 'not a square number'
    @property
    def n(self):
        return self.__n
    @n.setter
    def n(self, num):
        if type(num) == int and num > 0:
            self.__n = num
        else:
            self.__n = 1 # sensible default

if __name__ == '__main__':
    n = int(float(input('Enter a number: ')))
    r = NumberFun(n)
    print(r)
    # can we access name-mangled properties?
    # print( r.__num ) # fails
    r.__n = 99
    print(r.n)