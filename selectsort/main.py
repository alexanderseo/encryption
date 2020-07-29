import time
from selectsort.arrayselect import ArrayRandom
from selectsort.sortselect import SortSelect

if __name__ == "__main__":
    start_time = time.time()
    arr = ArrayRandom(10000)
    sorting = SortSelect(arr.displayarray())
    print('Оригинальный массив', arr.displayarray())
    print('Отсортированный массив', sorting.sortselection())
    print("--- %s время выполнения ---" % (time.time() - start_time))
