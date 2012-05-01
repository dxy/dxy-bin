#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2012 Daisuke Yabuki. All Rights Reserved.

"""Show the upcoming bus service from Roppongi to Shibuya.

This script gives the departure time of the next available bus service from
Roppongi Hills bound for Shibuya if no time is given as commandline option.
If time is given, this script gives the departure time for the bus service
departing after that time.

There are two routes from Roppongi to Shibuya in operation, RH01 and 都01,
so we combine timetables for those two routes and give the next available
bus service out of the combined timetable.

Caveat: This supports the timetable for weekdays only since I use this route
only on weekdays.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import argparse  # thus only supporting Python 2.7 or up
import datetime
import sys

# Route: RH01, bound for Shibuya, weekdays
# http://tobus.jp/cgi-bin/pctimetable.cgi?act=timel&bsn=13992480&lcd=TE090109&hcd=0
# Last checked: Apr 27, 2012
_TIMETABLE_RH01 = [
  [],  # 0 hour
  [],  # 1 hour
  [],  # 2 hour
  [],  # 3 hour
  [],  # 4 hour
  [],  # 5 hour
  [],  # 6 hour
  [],  # 7 hour
  [52,],  # 8 hour
  [15, 39,],  # 9 hour
  [0, 15, 30, 45,],  # 10 hour
  [0, 15, 30, 45,],  # 11 hour
  [0, 15, 30,],  # 12 hour
  [15,],  # 13 hour
  [1, 47,],  # 14 hour
  [33,],  # 15 hour
  [19,],  # 16 hour
  [4, 20, 35, 50,],  # 17 hour
  [6, 20, 35, 49,],  # 18 hour
  [4, 19, 33, 48,],  # 19 hour
  [3, 18, 33,],  # 20 hour
  [10,],  # 21 hour
  [0,],  # 22 hour
  [],  # 23 hour
]

# Route: 都01, bound for Shibuya, weekdays
# http://tobus.jp/cgi-bin/pctimetable.cgi?act=timel&bsn=13992480&lcd=TE090101&hcd=1
# Last checked: Apr 27, 2012
_TIMETABLE_M01 = [
  [],  # 0 hour
  [],  # 1 hour
  [],  # 2 hour
  [],  # 3 hour
  [],  # 4 hour
  [],  # 5 hour
  [],  # 6 hour
  [],  # 7 hour
  [15, 30, 44,],  # 8 hour
  [1, 10, 25, 34, 50,],  # 9 hour
  [8, 23, 39, 54,],  # 10 hour
  [9, 38, 54,],  # 11 hour
  [25, 52,],  # 12 hour
  [9, 32, 41,],  # 13 hour
  [13, 37, 50,],  # 14 hour
  [1, 7, 14, 46,],  # 15 hour
  [3, 36, 55,],  # 16 hour
  [27, 42,],  # 17 hour
  [25, 42,],  # 18 hour
  [56,],  # 19 hour
  [13, 52,],  # 20 hour
  [36,],  # 21 hour
  [25, 50,],  # 22 hour
  [],  # 23 hour
]


class NoServiceAvailable(Exception):
  pass


class CombinedRoutes:
  """Combined bus routes of RH01 and 都01.

  Attributes:
    timetable: A list describing the timetable of combined routes
        containing 24 lists with time of services for each hour in it.
  """

  def __init__(self):
    self._TIMETABLE_LENGTH = 24
    self._TIMETABLE_MAX_INDEX = self._TIMETABLE_LENGTH - 1

    self.timetable = []

    for timetable in [_TIMETABLE_RH01, _TIMETABLE_M01]:
      if len(timetable) != self._TIMETABLE_LENGTH:
        sys.stderr.write('invalid timetable length.')
        sys.exit(1)

    for hour in range(self._TIMETABLE_LENGTH):
      rh01 = set(_TIMETABLE_RH01[hour])
      m01 = set(_TIMETABLE_M01[hour])
      self.timetable.append(sorted(rh01.union(m01)))
      #print '{0:02d}: {1}'.format(hour, self.timetable[hour])

  def GetTimetable(self):
    return self.timetable

  def GetTimetableLength(self):
    return self._TIMETABLE_LENGTH

  def PickService(self, base_time, lead_time):
    """Pick bus services departing after base_time.

    Args:
      base_time: A datetime object describing a time to pick a bus service
          departing after that.
      lead_time: An integer representing a number of minutes one needs to get
          to the bus stop. You probably can't catch a bus leaving in 2 minutes
          if you run this script at your desk.

    Returns:
      A datetime object of the upcoming bus service meeting the given condition.

    Raises:
      NoServiceAvailable: No service available meeting the given condition.
    """
    candidate_services = []
    service_available = False

    def _PrepareCandidates(hour):
      services_of_the_hour = self.timetable[hour]
      now = datetime.datetime.now()
      for service_minute in services_of_the_hour:
        service = datetime.datetime(now.year, now.month, now.day,
                                    hour, service_minute)
        candidate_services.append(service)

    _PrepareCandidates(base_time.hour)

    # Let's add services of the next hour into candidate service list
    # in case that base_time is near the end of the hour and
    # there's none available in the hour.
    if base_time.hour < self._TIMETABLE_MAX_INDEX:
      _PrepareCandidates(base_time.hour + 1)
    #print candidate_services

    #print 'looking for service after {0:02d}:{1:02d}'.format(base_time.hour,
    #                                                         base_time.minute)
    delta = datetime.timedelta(minutes=lead_time)
    for candidate_service in candidate_services:
      if base_time + delta > candidate_service:
        continue  # Too late to catch this bus.
      # Congrats. Reaching here means you're lucky.
      service_available = True
      # TODO(dxy): allow this method to return 2 results instead of 1.
      return candidate_service
    if not service_available:
      raise NoServiceAvailable


def main():
  parser = argparse.ArgumentParser(description='Show the upcoming bus service '
                                   'from Roppongi to Shibuya.')
  parser.add_argument('--time', metavar='HH:MM', required=False,
                      help='Pick a bus after this time.')
  parser.add_argument('--lead_time', metavar='N', type=int, default=5,
                      required=False,
                      help=('Time to take for you to get to the bus stop'
                            'in minutes.'))
  parser.add_argument('--timetable', action='store_true',
                      required=False, default=False,
                      help='Show timetable.')
  args = parser.parse_args()

  service = None
  route = CombinedRoutes()

  # TODO(dxy): check the day of the week and if it's not weekday,
  # bail out.

  if args.time:
    try:
      hour, minute = args.time.split(':')
    except ValueError:
      sys.stderr.write('invalid time format')
      sys.exit(1)
    try:
      hour = int(hour)
      minute = int(minute)
    except ValueError:
      sys.stderr.write('invalid time format')
      sys.exit(1)
    today = datetime.datetime.today()
    base_time = datetime.datetime(today.year, today.month, today.day,
                                  hour, minute)
  else:
    base_time = datetime.datetime.now()

  try:
    service = route.PickService(base_time, args.lead_time)
  except NoServiceAvailable:
    sys.stderr.write('no service found')

  if service:
    print 'service departing at {0:02d}:{1:02d}'.format(service.hour,
                                                        service.minute)

  # TODO(dxy): make --timetable and others mutually-exclusive?
  if args.timetable:
    timetable = route.GetTimetable()
    for hour in range(route.GetTimetableLength()):
      services = timetable[hour]
      services_of_the_hour  = ' '.join('{0:02d}'.format(service)
                                       for service in services)
      print '{0:02d}: {1}'.format(hour, services_of_the_hour)

if __name__ == '__main__':
  main()
