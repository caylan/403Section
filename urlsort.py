"""
Usage: urlsort.py -f [FILE] -s [sorting algorithm] -o [OUT]
"""

import optparse
import random
import sys
import string
from sorters import *

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
               help="The sorted output will be printed to OUT (defaults to output.txt).",
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

    alg_list = [selectionsort, heapsort, mergesort, radixsort]
    sorter = alg_list[algorithm - 1]
    sorted_list = sorter.sort(unsorted)
    out = open(output, 'w')
    for url in sorted_list:
      out.write(url + "\n")
      
  except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

if __name__ == "__main__":
  main()
