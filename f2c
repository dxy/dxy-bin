#!/usr/bin/python
# Convert Fahrenheit to Celsius
# http://en.wikipedia.org/wiki/Fahrenheit

import sys

def Fahrenheit2Celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

def main():
  try:
    fahrenheit = float(sys.argv[1])
  except:
    sys.stderr.write('invalid argument\n')
    sys.exit(1)

  celsius = Fahrenheit2Celsius(fahrenheit)
  print celsius

if __name__ == '__main__':
  main()
