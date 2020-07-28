

class ArrayBub:
    def __init__(self, size):
        self.size = size
    def getarraybub(self):
        arr1 = [x for x in range(0, self.size, 3)]
        arr2 = [x for x in range(self.size, self.size + 300, 4)]
        arr3 = arr2[::-1] + arr1
        return arr3
