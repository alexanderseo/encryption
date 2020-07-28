

class SortBub:
    def __init__(self, arr):
        self.arr = arr

    def bubblesort(self):
        right_index = len(self.arr) - 1
        left_index = 0
        while left_index < right_index:
            j = 0
            while j < right_index - 1 - left_index:
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                j += 1
            left_index += 1
        return self.arr
