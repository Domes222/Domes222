import random
import copy
import sys


class Hat:
    contents = []

    def __init__(self, **kwargs):
        for i in kwargs.keys():
            for index in range(kwargs[i]):
                self.contents.append(i)
        if len(self.contents) < 1:
            print("Error not enough balls")
            sys.exit()

    def draw(self,number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        else:
            lst = copy.copy(self.contents)
            lst1 = []
            for i in range(number_of_balls):
                x = random.choice(lst)
                lst1.append(x)
                lst.remove(x)
            return lst1


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat1 = copy.deepcopy(hat)
    balls = []
    number_of_matches = 0
    for i in expected_balls.keys():
        for index in range(expected_balls[i]):
            balls.append(i)

    if len(hat1.contents) > num_balls_drawn:
        for w in range(num_experiments):
            draw = hat1.draw(num_balls_drawn)
            print(draw)
            print(balls)
            xx = 0
            for o in balls:
                if o in draw:
                    xx = xx + 1
                    draw.remove(o)
            if xx == int(len(balls)):
                number_of_matches += 1
    else:
        number_of_matches = num_experiments


    return number_of_matches

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=9,
                  num_experiments=2000)

print(probability)
