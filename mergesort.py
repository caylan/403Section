"""
Usage:
  import mergesort
  sorted_list = mergesort.sort(unsorted_list)
  print("hooray!")
"""

def sort(lst):
  if len(lst) <= 1:
    return lst
  mid = len(lst) / 2
  return merge(sort(lst[:mid]), sort(lst[mid:]))
  

def merge(left, right):
  merged = []
  l = r = 0
  while l < len(left) and r < len(right):
    if left[l] <= right[r]:
      merged.append(left[l])
      l += 1
    else:
      merged.append(right[r])
      r += 1
  return merged + left[l:] + right[r:]
