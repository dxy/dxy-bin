#!/usr/bin/python
# Copyright 2012 Daisuke Yabuki. All Rights Reserved.

"""Convert a string in YYYY/MM/DD format to unix timestamp.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import datetime
import time
import sys
from optparse import OptionParser

def main():
  usage = 'Usage: %s YYYY MM DD' % sys.argv[0]
  parser = OptionParser(usage=usage)
  (unused_options, args) = parser.parse_args()
  if len(args) != 3:
    parser.error('invalid arguments')

  year, month, day = args
  t = datetime.datetime(int(year), int(month), int(day))
  print "%s" % int(time.mktime(t.timetuple()))

if __name__ == '__main__':
  main()
