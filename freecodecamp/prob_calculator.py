import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        for color in kwargs:
            self.color = color

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return