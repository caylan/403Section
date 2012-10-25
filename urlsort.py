"""
Usage: urlsort.py -f [FILE] -s [sorting algorithm] -o [OUT]
"""

import optparse
import random
import sys
import string
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

def controller():
  p = optparse.OptionParser(description="URL Sorter. Takes in a file, "
                                        "sorts the URLs and then writes them "
                                        "to a file",
                          prog='urlsort.py',
                          version='0.1',
                          usage='%prog -f [FILE] -s [sorting algorithm] -o [OUT]')
  p.add_option('--file', '-f', dest="filename",
               help="The FILE from which we will read", metavar="FILE")
  p.add_option('--sort-alg', '-s', dest='algorithm',
               default=1, help='The type of sorting algorithm to use, '
                                  '1 = selection sort, '
                                  '2 = heap sort, '
                                  '3 = merge sort, '
                                  '4 = radix sort',
               metavar='ALG')
  p.add_option('--output', '-o', dest='output', default='output.txt',
               help="The sorted output will be printed to OUT.",
               metavar="OUT")
  (opts, args) = p.parse_args()
  return (p, opts, args)

def main():
  (parser, opts, args) = controller()
  if not opts.filename or not opts.algorithm or not opts.output:
    parser.print_help()
    sys.exit(1)

  try:
    algorithm = int(opts.algorithm)
  except:
    print("ERROR: invalid sorting algorithm, using default")
    algorithm = 1

  filename = opts.filename
  output = opts.output

  if algorithm < 1 or algorithm > 4:
    parser.print_help()
    sys.exit(1)
    
  try:
    f = open(filename, 'r')
    unsorted = read_file(f)
    
    if algorithm == 1:
      sorted_list = selectionsort.selection_sort(unsorted)
    elif algorithm == 2:
      sorted_list = heapsort.sort(unsorted)
    elif algorithm == 3:
      sorted_list = mergesort.sort(unsorted)
    else:
      sorted_list = radixsort.radixSort(unsorted)

    out = open(output, 'w')
    for url in sorted_list:
      print>>out, url
      
  except IOError:
    print('Unable to open file')

if __name__ == "__main__":
  main()
