#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2012 Daisuke Yabuki. All Rights Reserved.

"""Convert an integer to an IP address as a printable string.

Convert an integer to address family specific string representation
(i.e. dotted decimal notation for IPv4), e.g. 2130706433 to 127.0.0.1.

Samples:
127.0.0.1:
127 * (256 ** 3) + 0 * (256 ** 2) + 0 * 256 + 1 = 2130706433
\x7f\x00\x00\x01 in big endian, \x01\x00\x00\x7f in little endian
IP network byte order: big-endian, Intel: little-endian
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import optparse
import socket
import struct
import sys

def Number2Address(number):
  # upper_bound: 255 * (256 ** 3) + 255 * (256 ** 2) + 255 * 256 + 255
  #              = 4294967295
  upper_bound = 0xffffffff
  if number > upper_bound or number < 0:
    print 'invalid number for ip address'
    sys.exit(1)

  # !: network byte order (= big-endian), I: unsigned int
  packed_ip_address = struct.pack("!I", number)
  # TODO(dxy): IPv4 is so 20th century.
  return socket.inet_ntop(socket.AF_INET, packed_ip_address)

def main():
  try:
    number = int(sys.argv[1])
  except:
    print 'invalid value for ip address'
    sys.exit(1)
  print Number2Address(number)

if __name__ == '__main__':
  main()
