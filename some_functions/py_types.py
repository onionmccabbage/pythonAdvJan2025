# Python is a loosely typed language
# there are recent moves to implement data typing:

class Demo():
    def __init__(self) -> None:
        pass
    def oops(self)->None:
        return 'oops'
    

if __name__ == '__main__':
    d = Demo()
    print(  d.oops() )