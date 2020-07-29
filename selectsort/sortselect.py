

class SortSelect:
    def __init__(self, arr):
        self.arr = arr
    def sortselection(self):
        for i in range(0, len(self.arr) - 1):
            min_element = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_element]:
                    min_element = j
            self.arr[i], self.arr[min_element] = self.arr[min_element], self.arr[i]
        return self.arr
