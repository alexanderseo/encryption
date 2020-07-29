

class ArrayBub:
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected a INT')
        self._size = value

    def getarraybub(self):
        arr1 = [x for x in range(0, self.size, 3)]
        arr2 = [x for x in range(self.size, self.size + 300, 4)]
        arr3 = arr2[::-1] + arr1
        return arr3
