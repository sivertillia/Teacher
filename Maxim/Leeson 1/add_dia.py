from random import randint

class RandomDiagram():
    def __init__(self, num=5):
        self.num = num
        
        self.x_values = []
        self.y_values = []
    def dia_rand(self):
        while len(self.x_values) < self.num:
            x = randint(1, 100)
            y = str(x)
            if x not in self.x_values:
                self.x_values.append(x)
                self.y_values.append(y)