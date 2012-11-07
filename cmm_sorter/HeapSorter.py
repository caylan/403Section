'''
Created on Oct 23, 2012

@author: YoungMing
'''
from heapq import heappush, heappop


def sort(urls):
    heap = []
    ret = []
    for value in urls:
        heappush(heap, value)
    
    while(len(heap)>0):
        ret.append(heappop(heap))
    return ret