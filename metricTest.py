# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON

"""
Module metricTest.py
Metric example - Module which is used as a testbed for static
checkers.
This is a mix of different functions and classes doing different things.
 """

""" A function which performs a sum """

def fn(x, y):
    """ Function fn that return the sum of x and y"""
    return x + y

def optimal_route(expected_time, start_time,favorite_route='SBS1K', favorite_option='bus'):
    """  find_optimal_route_to_my_office_from_home """
    d = (expected_time - start_time).total_seconds() / 60.0
    if d <= 30:
        return 'car'

    # If d>30 but <45, first drive then take metro
    if d > 30 and d < 45:
        return ('car', 'metro')

    # If d>45 there are a combination of optionsWriting Modifiable and Readable Code
    # First volvo,then connecting bus

    if d > 45:
        if d < 60:
            return ('bus:335E', 'bus:connector')
        # Might as well go by normal bus # return random.choice(('bus:330','bus:331',':'))
    elif d > 80:
        ':'.join((favorite_option, favorite_route))
    elif d > 90:  # Relax and choose favorite route
        return ':'.join((favorite_option, favorite_route))

""" A class which does almost nothing """

class C_class():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f_function(self):
        """ Function f_function that doesn't do anything """
        pass

    def g_function(self, x, y):
        """ Function g to check """
        if self.x > self.x:
            return self.x + self.y
        elif self.x > self.x:
            return self.x + self.y

""" D class """
class D_class(C_class):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def f_function(self):
        """ Function that return the value of y + x """
        if self.x > self.y:
            return self.x - self.y
        return self.x + self.y

    def g_function(self):
        """ Function that return the value of y - x """
        if self.x > self.y:
            return self.x + self.y

        return self.y - self.x


