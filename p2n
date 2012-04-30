#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2012 Daisuke Yabuki. All Rights Reserved.

"""Convert an IP address from printable string to an integer.

Convert an IP address from its address family specific string format
(i.e. dotted decimal notation for IPv4) to an integer, e.g. 127.0.0.1
to 2130706433.

Samples:
127.0.0.1:
127 * (256 ** 3) + 0 * (256 ** 2) + 0 * 256 + 1 = 2130706433
\x7f\x00\x00\x01 in big endian, \x01\x00\x00\x7f in little endian
IP network byte order: big-endian, Intel: little-endian

http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
is semi interesting discussion, btw.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import optparse
import socket
import struct
import sys

def Address2Number(ip_address):
  # TODO(dxy): IPv4 is so 20th century.
  try:
    packed_ip_address = socket.inet_pton(socket.AF_INET, ip_address)
  except socket.error:
    print 'invalid address'
    sys.exit(1)

  # !: network byte order (= big-endian), I: unsigned int
  number = struct.unpack("!I", packed_ip_address)
  return number[0]

def main():
  usage = 'Usage: %s a.b.c.d' % sys.argv[0]
  parser = optparse.OptionParser(usage=usage)
  (unused_options, args) = parser.parse_args()
  if len(args) != 1:
    parser.error('invalid arguments')

  ip_address = args[0]
  print Address2Number(ip_address)


if __name__ == '__main__':
  main()
