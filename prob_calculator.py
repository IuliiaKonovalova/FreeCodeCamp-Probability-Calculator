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

    def get_contents(self):
        """
        Returns self content of the Hat class
        """
        return self.contents

    def draw(self, number):
        """
        Accepts a number of balls to draw,
        Removes balls at random from self.contents list,
        if number of balls to draw exceeds the available quantity,
        returns all balls in the Hat.
        """
        all_removed = []
        if number > len(self.contents):
            return self.content
