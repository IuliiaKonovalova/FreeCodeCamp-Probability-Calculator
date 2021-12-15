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
        removed_balls = []
        if number > len(self.contents):
            return self.contents
        else:
            for i in range(number):
                removed_ball = self.contents.pop(
                    int(random.random() * len(self.contents))
                )
                removed_balls.append(removed_ball)
                return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    returns the probability
    """
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)
        for color in colors_gotten:
            if color in expected_copy:
                expected_copy[color] =- 1
        if all(x <= 0 for x in expected_copy.values()):
            count += 1
    return count / num_experiments
