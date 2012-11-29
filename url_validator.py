#!/usr/bin/env python
"""
Usage: urlsort.py -f [FILE] -s [sorting algorithm] -o [OUT]
"""

import optparse
import random
import codecs
import sys
import string

from sorters import heapsort
from url_util import *

def controller():
  '''
  Parses the command line arguments and returns the newly created parser,
  the arguments that have been parsed, and the options that have been parsed.
  '''
  p = optparse.OptionParser(description="URL Validator. Takes in a file, "
                                        "normalizes valid URLs and then writes them "
                                        "to a file",
                          prog='urlsort.py',
                          version='0.1',
                          usage='%prog -v [int] -f [FILE] -o [OUT]')
  p.add_option('--file', '-f', dest="filename",
               help="The FILE from which we will read", metavar="FILE")

  p.add_option('--output', '-o', dest='output', default='output.txt',
               help="The sorted output will be printed to OUT (defaults to output.txt).",
               metavar="OUT")
  (opts, args) = p.parse_args()
  return (p, opts, args)

def handle_io_exception(f, ex):
    print("I/O error({1}) -- \"{0}\" : {2}".format(f, ex.errno, ex.strerror))
    sys.exit(1)

def unicode_print(string):
    '''
    Works around not being able to properly print a unicode string.  This
    should, hopefully, print out an escaped string instead.  This only really
    shows up as an issue in python2.7 as opposed to python3 for some reason.
    '''
    try:
        print(string)
    except UnicodeEncodeError:
        print(string.encode('unicode-escape'))

def normalize_url_list(url_lst):
    '''
    Normalizes and validates a list of URLs.  While doing this, the outcome of
    each URL is printed to stdout.
    '''
    normal_url_set = set()
    url_set = set()
    for url in url_lst:
        print("> Source:")
        unicode_print(url)

        valid = is_valid_url(url)
        unique = url not in url_set
        normal_url = u"N/A"
        url_set = url_set.union([url])
        if valid:
            normal_url = normalize_url(url)
            normal_unique = normal_url not in normal_url_set
            normal_url_set = normal_url_set.union([normal_url])
    
        # Now print out the data in a silly ordering.
        normal_url.encode('utf-8')
        print("> Valid: {0}".format(str(valid)))
        unicode_print(u"> Canonical: {0}".format(normal_url))
        print("> Source unique: {0}".format(str(unique)))
        if valid:
            unicode_print(u"> Canonicalized URL unique: {0}".format(\
                            str(normal_unique)))
    return list(normal_url_set)

def main():
  '''
  Takes in the command line arguments, selects a sorter,
  and then sorts the URLs.  After they've been sorted, the 
  URLs are written out to a file the user has selected (else
  the default file).
  '''
  (parser, opts, args) = controller()
  if not opts.filename or not opts.output:
    parser.print_help()
    sys.exit(1)

  filename = opts.filename
  output = opts.output

  try:
    f = codecs.open(filename, encoding='utf-8', mode='r')
    urls = [l for l in [line.strip() for line in f.readlines()] if l != u'']
  except IOError as e:
    handle_io_exception(filename, e) 

  try:  
    # Normalize the URLs and print out the details.
    urls = normalize_url_list(urls)
    sorted_list = heapsort.sort(urls)

    # Write out the sorted list of valid normalized URLs to the output file.
    out = codecs.open(output, encoding='utf-8', mode='w')
    for url in sorted_list:
      out.write(url + "\n")
  except IOError as e:
    handle_io_exception(output, e)

if __name__ == "__main__":
  main()
