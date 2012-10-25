"""
Usage: python urlsort.py [filename] [sorting algorithm: (1-4)]
1: Selection sort
2: Heap sort
3: Merge sort
4: Radix sort
"""

import optparse
import random
import sys
import string
import selectionsort
import heapsort
import mergesort
import radixsort

def url_generator(size=20, chars=string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def list_make():
        thelist = []
        for x in range(5):
                thelist.append(url_generator())
        thefile = open("output.txt", 'w')
        for item in thelist:
                thefile.write("www.%s.com\n" % item)

def test_list():
        f = open("output.txt", 'r')
        list_sorted = read_file(f)
        working = "working"
        for x in range(len(list_sorted)-1):
                if list_sorted[x] > list_sorted[x+1]:
                        working = "not working"
        print(working)

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
                          usage='%prog -f [file] -s [sorting algorithm]')
  p.add_option('--file', '-f', dest="filename",
               help="The FILE from which we will read", metavar="FILE")
  p.add_option('--sort-alg', '-s', dest='algorithm',
               default=1, help='The type of sorting algorithm to use, '
                                  '1 = selection sort, '
                                  '2 = heap sort, '
                                  '3 = merge sort, '
                                  '4 = radix sort',
               metavar='ALG')
  p.add_option('--output', '-o', dest='output',
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

  if algorithm < 1 or algorithm > 4:
    parser.print_help()
    sys.exit(1)
    
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
