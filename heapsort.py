from heapq import *

def sort(lst):
  heap = list(lst)
  heapify(heap)
  for i in range(len(lst)):
    lst[i] = heappop(heap)
  return lst
