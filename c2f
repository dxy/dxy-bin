#!/usr/bin/python
# Convert Celsius to Fahrenheit
# http://en.wikipedia.org/wiki/Fahrenheit

import sys

def Celsius2Fahrenheit(celsius):
  fahrenheit = (celsius * 9 / 5) + 32
  return fahrenheit

def main():
  try:
    celsius = float(sys.argv[1])
  except:
    sys.stderr.write('invalid argument\n')
    sys.exit(1)

  fahrenheit = Celsius2Fahrenheit(celsius)
  print fahrenheit

if __name__ == '__main__':
  main()
