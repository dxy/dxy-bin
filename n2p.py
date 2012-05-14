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

def Number2Ipv4Address(number):
  # upper_bound: 255 * (256 ** 3) + 255 * (256 ** 2) + 255 * 256 + 255
  #              = 4294967295
  upper_bound = 0xffffffff
  if number > upper_bound or number < 0:
    sys.stderr.write('invalid number for ip address\n')
    sys.exit(1)

  # !: network byte order (= big-endian), I: unsigned int
  packed_ip_address = struct.pack("!I", number)
  # TODO(dxy): IPv4 is so 20th century.
  return socket.inet_ntop(socket.AF_INET, packed_ip_address)

def Number2Ipv6Address(number):

  if number < 0:
    sys.stderr.write('invalid number for ip address\n')
    sys.exit(1)

  # Q: unsigned long long (8-byte)
  packed_ip_address = struct.pack("!QQ",
                                  number >> 64,
                                  number & 0xffffffffffffffff)
  return socket.inet_ntop(socket.AF_INET6, packed_ip_address)

def main():
  usage = "usage: %prog [option] address_in_number"
  parser = optparse.OptionParser(usage=usage)
  parser.add_option("-4", "--ipv4", dest="address_family",
                    action="store_const", const=4,
                    help="IPv4 address is given.")
  parser.add_option("-6", "--ipv6", dest="address_family",
                    action="store_const", const=6,
                    help="IPv6 address is given.")
  (options, args) = parser.parse_args()
  try:
    #number = int(sys.argv[1])
    number = int(args[0])
  except:
    sys.stderr.write('invalid value for ip address\n')
    sys.exit(1)
  if options.address_family == 4:
    print Number2Ipv4Address(number)
  elif options.address_family == 6:
    print Number2Ipv6Address(number)
  else:
    sys.stderr.write('invalid address family\n')
    sys.exit(1)

if __name__ == '__main__':
  main()
