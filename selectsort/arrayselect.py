import random

class ArrayRandom:
    def __init__(self, size):
        self.size = size
    def displayarray(self):
        arr = []
        for x in range(self.size):
            x = random.randint(1, 99)
            arr.append(x)
        return arr
