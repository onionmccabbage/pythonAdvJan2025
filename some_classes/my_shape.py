from basic_classes import AbstractShape

class Shape(AbstractShape):
    '''This shape will have a number of sides'''
    def __init__(self, num_sides):
        '''This method is called every time we create an instance'''
        self.num_sides = num_sides
    # we may declare property getters and setters
    @property
    def num_sides(self):
        return self.__num_sides
    @num_sides.setter
    def num_sides(self, num_sides):
        self.__num_sides = num_sides
    # we must implement a __str__ method
    def __str__(self):
        return f'this is my shape with {self.__num_sides} sides'

if __name__ == '__main__':
    # make an instance of our class
    triangle = Shape(3)
    print(triangle)