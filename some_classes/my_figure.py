from my_shape import Shape

class Figure(Shape): # we now have all the fatures of the Shape class
    # we may give properties to the class itself (not to any particluar instance)
    count = 0
    def __init__(self, num_sides, colour, id):
        super().__init__(num_sides, colour) # call the init of the parent class
        self.id = id
        Figure.count += 1 # increase the count every t ime we make a new instance
    @classmethod
    def howMany(cls): 
        '''This method belongs to the class (not to any particular instance)'''
        return f'There are {cls.count} instances of this class'
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError('ID must be an integer')
    # we may choose to override other methods of hte parent class
    def __str__(self):
        return f'This figure id:{self.id} has {self.num_sides} sides and is {self.colour}'

if __name__ == '__main__':
    fig1 = Figure(5, 'pink', 44)
    fig2 = Figure(2, 'grey', 45)
    fig3 = Figure(6, 'yellow', 46)
    fig4 = Figure(3, 'vermillion', 47)
    print(fig1)
    print(Figure.howMany())

