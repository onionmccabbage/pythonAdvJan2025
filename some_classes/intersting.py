

class Something():
    def n(self):
        '''This function belongs to the class AND to every instance of the class     
        '''
    def k(): # we may chose to pass any other params in here
        '''this function ONLY exists on the Class not on any instace'''

s =Something()
s.n()
# s.k() # fail
Something.k()