#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2009 Daisuke Yabuki. All Rights Reserved.

"""Convert a string to a series of NATO phonetic alphabet.

This script is what I was using until I remember phonetic alphabet by heart.
It takes a string and gives you back the string in a series of phonetic
alphabet (e.g. 'foxtrot lima alpha golf' for 'flag').

At one company, I needed to pass along a root password which was just updated
to an incoming oncall person at the end of my shift on phone from time to time.

It really helps to use NATO phonetic alphabet in such situations so that
'b' and 'p' or 't' and 'd' are not confused, especially when the person on the
other end of the phone connection has engineering background and is familiar
with phonetic alphabet.

On Mac OS X, "say $(path/to/phonetic.py 'lucy in the sky with diamonds')"
would let your Mac speak 'lima uniform charlie yankee ...'.

On Solaris, I used to use festival as speech synthesizer to let my Ultra 1
speak for my personal programmable voice mail project back in late 90s.
So you might want to try that on Linux/*BSD/Solaris.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

from optparse import OptionParser
import sys


class Phonetic(object):
  def __init__(self):
    self.PHONETIC_TABLE = {
      'a': 'alpha',    'b': 'bravo',    'c': 'charlie',  'd': 'delta',
      'e': 'echo',     'f': 'foxtrot',  'g': 'golf',     'h': 'hotel',
      'i': 'india',    'j': 'juliet',   'k': 'kilo',     'l': 'lima',
      'm': 'mike',     'n': 'november', 'o': 'oscar',    'p': 'papa',
      'q': 'quebec',   'r': 'romeo',    's': 'sierra',   't': 'tango',
      'u': 'uniform',  'v': 'victor',   'w': 'whisky',   'x': 'x-ray',
      'y': 'yankee',   'z': 'zulu'
    }

  def _ConvertCharacterToPhonetic(self, char):
    phonetic = ''
    try:
      phonetic = self.PHONETIC_TABLE[char]
    except KeyError:
      phonetic = char
    return phonetic

  def Process(self, text):
    phonetics = []
    for char in text:
      phonetics.append(self._ConvertCharacterToPhonetic(char))
    return phonetics


class ExtendedPhonetic(Phonetic):
  def __init__(self):
    Phonetic.__init__(self)
    PHONETIC_TABLE_EXTENSION = {
      '/': 'forwardslash',      '_': 'underscore',
      '!': 'exclamation-mark',  '?': 'question-mark',
      '#': 'pound',             '@': 'at-mark',
      '.': 'dot',               ',': 'comma',
      ':': 'colon',             ';': 'semicolon',
      '*': 'asterisk',          '%': 'percent',
      '&': 'ampersand',         '$': 'dollar',
      '<': 'less-than',         '>': 'greater-than',
      '-': 'dash'
    }
    self.PHONETIC_TABLE.update(PHONETIC_TABLE_EXTENSION)

  def _ConvertCharacterToPhonetic(self, char):
    case = ''
    if char.isalpha():
      if char.isupper():
        case = '(uppercase)'
      else:
        case = '(lowercase)'

    phonetic = ''
    try:
      phonetic = self.PHONETIC_TABLE[char.lower()]
    except KeyError:
      phonetic = char

    return case + phonetic


def main():
  usage = 'usage: %s string' % sys.argv[0]
  parser = OptionParser(usage=usage)
  (unused_options, args) = parser.parse_args()
  if len(args) != 1:
    parser.error('one and only one argument expected')

  phonetic = ExtendedPhonetic()
  print ' '.join(phonetic.Process(args[0]))

if __name__ == '__main__':
  main()
