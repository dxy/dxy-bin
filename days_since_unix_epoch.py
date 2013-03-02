#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2013 Daisuke Yabuki. All Rights Reserved.

"""Calculate an index number for a given date.

This calculates an index number for a given date, which is approximately
equal to the number of days since Jan 1, 1900.

A spreadsheet of daily foreign exchange rate which is downloadable via
http://www.murc-kawasesouba.jp/fx/past_3month.php
shows each date as something as follows:
Sun, 2012/01/01 as 40909
Mon, 2012/01/02 as 40910
and so on.

In order to get foreign exchange rate (TTM) for USDJPY, for example, for a given
date, which is necessary to file a tax return including stock options and
whatnot, you need to find a right index number for the date in the spreadsheet.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import datetime
import sys
import argparse

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
  # off. so the adjustment is made blindly in order to get the expected output.
  parser.add_argument('--adjustment', metavar='n', nargs='?', type=int,
                      default=2,
                      help='adjustment value')
  parser.add_argument('--date', metavar='YYYY-MM-DD',
                      help='the date to get the index value for.')
  args = parser.parse_args()

  try:
    year, month, day = args.date.split('-')
  except ValueError:
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

  epoch = datetime.datetime(1900, 1, 1)
  delta = t - epoch
  print delta.days + args.adjustment  # to make 2012/01/01 match to 40909

if __name__ == '__main__':
  main()
