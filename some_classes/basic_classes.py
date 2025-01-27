class A:
    pass

class B():
    pass

class C(object):
    pass

class D(dict):
    pass

# Sometimes its useful to inherit from an Abstraction
from abc import ABCMeta, abstractmethod

class AbstractShape(metaclass=ABCMeta): # we now have an abstract class
    '''Abstraction means we can declare properties and methods
    that we willneed to implement in concrete classes'''
    @property # we may declare abstract properties
    @abstractmethod
    def num_sides(self, num_sides):
        pass # we make no implementation code within abstract