from basic_classes import AbstractShape

class Shape(AbstractShape):
    '''This shape will have a number of sides'''
    __slots__ = ('__num_sides','__colour') # a tuple of permitted properties of this class
    def __init__(self, num_sides, colour):
        '''This method is called every time we create an instance'''
        self.num_sides = num_sides # here we are calling the setter methods of this class
        self.colour    = colour
    # we may declare property getters and setters
    @property
    def num_sides(self):
        # we use name mangling to prevent direct access to properties of this class
        return self.__num_sides
    @num_sides.setter
    def num_sides(self, num_sides):
        # carry out validation
        if type(num_sides) == int and num_sides>0:
            self.__num_sides = num_sides
        else:
            raise TypeError('Shapes must have a positive ineger number of sides')
    # we must implement a __str__ method
    @property
    def colour(self):
        return self.__colour
    @colour.setter
    def colour(self, colour):
        if type(colour)==str and colour != "":
            self.__colour = colour
        else:
            self.__colour = 'white' # sensible default
    def __str__(self):
        return f'this is my shape with {self.num_sides} sides, colour is {self.colour}'

if __name__ == '__main__':
    # make an instance of our class
    triangle = Shape(3, 'blue')
    # attempt to add arbitrary property to our class
    triangle.__best_before = 9 # this is an arbitrary property....
    print(triangle)