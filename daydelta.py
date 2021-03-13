#!/usr/bin/python

import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('date', nargs=2)
args = parser.parse_args()

def str2date(s):
  # TODO(dxy): Validate that s is in "YYYY-MM-DD" format.
  tokens = s.split('-')
  y, m, d = [int(s) for s in tokens]
  return datetime.date(y, m, d)

print(str2date(args.date[1]) - str2date(args.date[0]))


