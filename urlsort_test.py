"""
Usage: python urlsort_test.py [-g | -t]
-g: Generate a file of URLs, testurls.txt
-t: Test that the file output.txt is sorted correctly
"""

import sys
import string
import random
import urlsort

def url_generator(size=20, chars=string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def list_make():
  thelist = []
  for x in range(10):
    thelist.append(url_generator())
  thefile = open("testurls.txt", 'w')
  for item in thelist:
    thefile.write("www.%s.com\n" % item)

def test_list():
  f = open("output.txt", 'r')
  list_sorted = urlsort.read_file(f)
  working = "working"
  for x in range(len(list_sorted)-1):
    if list_sorted[x] > list_sorted[x+1]:
      working = "not working"
  print(working)

def main():
  argv = sys.argv

  if argv[1] == '-g':
    list_make()
  if argv[1] == '-t':
    test_list()

if __name__ == "__main__":
  main()