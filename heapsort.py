from heapq import *

class Sorter():
  def sort(self, lst):
    pass

class HeapSort(Sorter):
  def sort(self, lst):
    heap = list(lst)
    heapify(heap)
    for i in range(len(lst)):
      lst[i] = heappop(heap)
    return lst
