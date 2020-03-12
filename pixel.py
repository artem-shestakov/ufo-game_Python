class Pixel:
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_value):
        self.__x = new_value
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_value):
        self.__y = new_value

    def __iadd__(self, other):
        if isinstance(other, Pixel):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, tuple):
            self.x += other[0]
            self.y += other[1]
        else:
            self.x += other
            self.y += other
        return self
    
    def __add__(self, other):
        if isinstance(other, Pixel):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self
    __radd__ = __add__

    def move(self, next_point):
        return self.__add__(next_point)
    
    def coor(self):
        return self.__x, self.__y