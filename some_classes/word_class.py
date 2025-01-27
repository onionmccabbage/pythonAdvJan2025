# we need a case-insensitive equality operators for words (strings)

class Word(): # here we choose to inherit from object (implicitly)
    '''Encapsulate a case-blind string'''
    def __init__(self, word):
        self.word = word # NB no validation, no property methods, just plain old setting value
    def __eq__(self, otherWord): 
        '''We override the built-in equlaity operator''' 
        return str(self.word).lower() == str(otherWord.word).lower()       

if __name__ == '__main__':
    # exercise our code
    w1 = 'hello'
    w2 = 'Hello'
    print(w1 == w2) # False
    print(w1.lower() == w2.lower() ) # True
    # exercise our 'Word' class
    W1 = Word('hello')
    W2 = Word('Hello')
    print(W1==W2) # this will use our overriden equality operator - True