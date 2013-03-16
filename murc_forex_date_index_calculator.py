#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2013 Daisuke Yabuki. All Rights Reserved.

"""Calculate an index number for a given date.

This calculates an index number for a given date, which is approximately
equal to the number of days since Jan 1, 1900.

An xls file of daily foreign exchange rate, murc_2012.xls, which is
downloadable via http://www.murc-kawasesouba.jp/fx/past_3month.php
shows each date as follows:
40909 for Sun, 2012/01/01
40910 for Mon, 2012/01/02
and so on.

In order to get foreign exchange rate (TTM) for USDJPY=X, for example, on a
given date, which is necessary to file a tax return including income from
stock options and/or ESOP, you need to find a right index number for data
on a particular date in the xls file.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import argparse
import datetime
import sys

def main():
  def _IsInteger(val):
    try:
      int(val)
      return True
    except ValueError:
      return False
    except TypeError:
      return False

  parser = argparse.ArgumentParser()
  # Without this adjustment, 2012/01/01 turns out to be 40907, which is 2 days
  # off from what one sees on the spreadsheet. so the adjustment is made
  # blindly in order to get the expected output.
  parser.add_argument('--offset', metavar='n', nargs='?', type=int, default=2,
                      help='offset value for adjustment')
  parser.add_argument('--date', metavar='YYYY-MM-DD',
                      help='the date to get the index value for.')
  args = parser.parse_args()

  try:
    year, month, day = args.date.split('-')
  except (ValueError, AttributeError):
    sys.stderr.write('invalid date\n')
    sys.exit(1)

  for val in year, month, day:
    if not _IsInteger(val):
      sys.stderr.write('invalid date\n')
      sys.exit(1)

  if int(year) < 1900:
    sys.stderr.write('the date needs to be in or after year 1900\n')
    sys.exit(1)

  try:
    t = datetime.datetime(int(year), int(month), int(day))
  except ValueError:
    sys.stderr.write('invalid date\n')
    sys.exit(1)

  origin = datetime.datetime(1900, 1, 1)
  delta = t - origin
  print '%s %s' % (# to make 2012/01/01 match to 40909
                   delta.days + args.offset,
                   t.strftime('%a'))

if __name__ == '__main__':
  main()
