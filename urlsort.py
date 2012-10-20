"""
Usage: python urlsort.py [filename] [sorting algorithm: (1-4)]
1: blasort
2: blablasort
3: blablablasort
4: blablablablasort
"""

USAGE = 'Usage: python urlsort.py [filename] [sorting algorithm: (1-4)]'

import sys

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