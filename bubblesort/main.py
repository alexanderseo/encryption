from bubblesort.arraybub import ArrayBub
from bubblesort.sortbub import SortBub
import time


if __name__ == "__main__":
    start_time = time.time()
    arr = ArrayBub(30000)
    sorting = SortBub(arr.getarraybub())
    print('Оригинальный массив', arr.getarraybub())
    print('Отсортированный массив', sorting.bubblesort())
    print("--- %s время выполнения ---" % (time.time() - start_time))