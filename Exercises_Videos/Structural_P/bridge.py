"""Barbara Rodríguez López"""
"""GITI9071"""
"""Bridge Dslink an abstraction of its implementation"""

class DrawingAPIOne(object):
    """Implementation-specific abstracion: concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class DrawingAPIOTwo(object):
    """Implementation-specific abstraction: concrete class two"""
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class Circle(object):
    """Implementation-specific abstraction: for example, there could be a rectangle class!"""

    def __init__(self, x, y , radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction take care of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)


    def scale(self, percent):
        """Implementation-independent"""
        self._radius *= percent

#Bulid the first cicle object using API one
circle1 = Circle(1, 2, 3, DrawingAPIOne())

#Draw a circle
circle1.draw()

#Build the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPIOTwo())

#Draw a circle
circle2.draw()