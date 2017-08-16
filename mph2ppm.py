#!/usr/bin/python
"""Convert running speed in mph to pace per mile."""

import optparse
import datetime

def Mph2Ppm(mph):
  """Convert miles per hour to pace per mile.
  """
  mile_travel_duration_in_sec = 3600 / mph
  d = datetime.timedelta(seconds=mile_travel_duration_in_sec)
  return str(d).split('.')[0]

def main():
  parser = optparse.OptionParser()
  (options, args) = parser.parse_args()
  mph = float(args[0])
  print Mph2Ppm(mph)

if __name__ == '__main__':
  main()
