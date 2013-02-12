#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2013 Daisuke Yabuki. All Rights Reserved.

"""Calculate N days from a given date.

This is originally written to calculate the date 90 days from the present day
in order to find the next refill date of T-Mobile prepaid SIM cards, although
I suspect perhaps this can be achieved with some date(1) trick.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import argparse
import datetime

def CalculateTarget(delta_days):
  d = datetime.timedelta(days=delta_days)
  now = datetime.datetime.now()
  target = now + d
  return target

def main():
  parser = argparse.ArgumentParser()
  # TODO(dxy): Allow the base date a command line parameter.
#  parser.add_argument('base', metavar='YYYYMMDD', nargs='?', type=int,
#                      help='a string of a base date.')
  parser.add_argument('delta', metavar='D', nargs='?', type=int, default=90,
                      help='an integer for the number of days from base date.')
  args = parser.parse_args()
  target = CalculateTarget(args.delta)
  print target

if __name__ == '__main__':
  main()