"""
Usage: python urlsort.py [filename] [sorting algorithm: (1-4)]
1: Selection sort
2: Heap sort
3: Merge sort
4: Radix sort
"""

USAGE = 'Usage: python urlsort.py [filename] [sorting algorithm: (1-4)]'

import sys
import selectionsort
import heapsort
import mergesort
import radixsort

def read_file(f):
  urls = []
  url = ''
  for line in f:
    url = line.strip()
    if url != '':
      urls.append(url)
  return urls

def main():
  argv = sys.argv
  if len(argv) < 3:
    print USAGE
    sys.exit()
  
  filename = argv[1]
  algorithm = int(argv[2])
  
  if algorithm < 1 or algorithm > 4:
    print USAGE
    sys.exit()
    
  try:
    f = open(filename, 'r')
    unsorted = read_file(f)
    
    print unsorted
    
    if algorithm == 1:
      sorted_list = selectionsort.selection_sort(unsorted)
    elif algorithm == 2:
      sorted_list = heapsort.sort(unsorted)
    elif algorithm == 3:
      sorted_list = mergesort.sort(unsorted)
    else:
      sorted_list = radixsort.radixSort(unsorted)

    out = open('output.txt', 'w')
    for url in sorted_list:
      print>>out, url

  except IOError:
    print 'Unable to open file'

if __name__ == "__main__":
  main()