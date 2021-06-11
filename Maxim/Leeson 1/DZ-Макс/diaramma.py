from matplotlib import pyplot as plt
from random import randint
class create_diagramm():

    def __init__(self, num=5):
        self.num = num
        self.x_value = [1]
        self.y_value = [0]



    def fill_array(self):
        x = 0
        while len(self.x_value) <= self.num:
            y = randint(1, 100)
            x += 1
            self.x_value.append(x)
            self.y_value.append(y)