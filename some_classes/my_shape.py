from basic_classes import AbstractShape

class Shape(AbstractShape):
    '''This shape will have a number of sides'''
    
    @property
    def num_sides(self, num_sides):
        self.__num_sides = num_sides
    # we must implement a __str__ method
    def __str__(self):
        return f'this is my shape'

if __name__ == '__main__':
    # make an instance of our class
    triangle = Shape()
    print(triangle)