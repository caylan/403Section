from heapq import *

def sort(self, lst):
  heap = list(lst)
  heapify(heap)
  for i in range(len(lst)):
    lst[i] = heappop(heap)
  return lst
