"""
Usage: python urlsort.py [filename] [sorting algorithm: (1-4)]
1: blasort
2: blablasort
3: blablablasort
4: blablablablasort
"""

USAGE = 'Usage: python urlsort.py [filename] [sorting algorithm: (1-4)]'

import sys
import string
import random

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
      print 'TODO'
    elif algorithm == 2:
      print 'TODO 2'
    elif algorithm == 3:
      print 'TODO 3'  
    else:
      print 'TODO 4'    
    
  except IOError:
    print 'Unable to open file'

if __name__ == "__main__":
  main()