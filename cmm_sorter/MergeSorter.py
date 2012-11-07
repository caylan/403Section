'''
Created on Oct 23, 2012

@author: Joon
'''

def _merge(left, right):
    i = 0
    j = 0
    sort = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sort.append(left[i])
            i += 1
        else:
            sort.append(right[j])
            j += 1
            
    while i < len(left):
        sort.append(left[i])
        i += 1
        
    while j < len(right):
        sort.append(right[j])
        j += 1
            
    return sort

def sort(urls):
    if len(urls) <= 1:
        return urls
    
    mid = len(urls) / 2
    left = sort(urls[:mid])
    right = sort(urls[mid:])
    return _merge(left, right)
