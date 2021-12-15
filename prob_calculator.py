import copy
import random

class Hat:
    """
    Takes multiple arguments: color of the balls and the number of the balls of
    a particular color.
    Consist draw method that removes given balls at random
    """

    def __init__(self, **kwargs):
        """
        Takes multiple arguments with keys and values and transform them into a 
        list with multiple string of keys.
        The number of repeating keys depends on the value given 
        """
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
