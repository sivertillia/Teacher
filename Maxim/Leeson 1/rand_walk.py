from random import randint

class RandowWalk():
    def __init__(self, num=50000):
        self.num = num

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num:
            x = randint(0, 10000)
            y = randint(0, 10000)
            self.x_values.append(x)
            self.y_values.append(y)