#!/usr/bin/env python
"""
Usage: urlsort.py -f [FILE] -s [sorting algorithm] -o [OUT]
"""

import optparse
import random
import sys
import string

from sorters import *
from cmm_sorter import *  # change my mood's sorting algorithms

def read_file(f):
  '''
  Reads in a file line by line, creating an array of strings.
  '''
  urls = []
  url = ''
  for line in f:
    url = line.strip()
    if url != '':
      urls.append(url)
  return urls

def controller():
  '''
  Parses the command line arguments and returns the newly created parser,
  the arguments that have been parsed, and the options that have been parsed.
  '''
  p = optparse.OptionParser(description="URL Sorter. Takes in a file, "
                                        "sorts the URLs and then writes them "
                                        "to a file",
                          prog='urlsort.py',
                          version='0.1',
                          usage='%prog -v [int] -f [FILE] -s [sorting algorithm] -o [OUT]')
  p.add_option('--valid', '-v', dest='int', default=0,
               help='The type of URL validation to use (defaults to zero), '
               '0 = all URLs, '
               '1 = valid URLs, '
               '2 = invalid URLs')
  p.add_option('--file', '-f', dest="filename",
               help="The FILE from which we will read", metavar="FILE")
  p.add_option('--sort-alg', '-s', dest='algorithm',
               default=1, help='The type of sorting algorithm to use (defaults to one), '
                                  '1 = selection sort, '
                                  '2 = heap sort, '
                                  '3 = merge sort, '
                                  '4 = radix sort. '
                                  'Change My Mood sorters: '
                                  '5 = binary sort, '
                                  '6 = heap sort, '
                                  '7 = insertion sort, '
                                  '8 = merge sort',
               metavar='ALG')
  p.add_option('--output', '-o', dest='output', default='output.txt',
               help="The sorted output will be printed to OUT (defaults to output.txt).",
               metavar="OUT")
  (opts, args) = p.parse_args()
  return (p, opts, args)

def handle_io_exception(f, ex):
    print("I/O error({1}) -- \"{0}\" : {2}".format(f, ex.errno, ex.strerror))
    sys.exit(1)


def main():
  '''
  Takes in the command line arguments, selects a sorter,
  and then sorts the URLs.  After they've been sorted, the 
  URLs are written out to a file the user has selected (else
  the default file).
  '''
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

  if algorithm < 1 or algorithm > 8:
    parser.print_help()
    sys.exit(1)
    
  try:
    f = open(filename, 'r')
    unsorted = read_file(f)
  except IOError as e:
    handle_io_exception(filename, e) 

  try:
    '''
    Grab the algorithm from the list of imported modules.  Why this order?
    Because we can!
    '''
    alg_list = [selectionsort, heapsort, mergesort, radixsort,
                BinarySorter, HeapSorter,
                InsertionSorter, MergeSorter,]
    sorter = alg_list[algorithm - 1]
    sorted_list = sorter.sort(unsorted)
    out = open(output, 'w')
    for url in sorted_list:
      out.write(url + "\n")
  except IOError as e:
    handle_io_exception(output, e)

if __name__ == "__main__":
  main()
