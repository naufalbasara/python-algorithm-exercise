import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, n):
        n = n if len(self.contents) > n else len(self.contents)
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    
    for _ in range(num_experiments):
        hat_2 = copy.deepcopy(hat)
        balls_drawn = hat_2.draw(num_balls_drawn)
        balls_get = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_get == len(expected_balls) else 0
    output = m/num_experiments

    return output