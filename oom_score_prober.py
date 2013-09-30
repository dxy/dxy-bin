#!/usr/bin/python

"""Checks OOM Killer parameters for each process on the system.

This script traverses /proc file system tree for OOM Killer parameters
(i.e. badness or oom_score etc.) for each process on the system.

cf. https://lwn.net/Articles/391222/ among other LWN articles.
oom_adj: deprecated
oom_score_adj: the knob you use to tweak (1000: kill me, -1000: disable oom
               kills entirely)
"""

import os
import sys

def TraverseProcfs():
  _PROCFS_ROOT = '/proc'
  procs = []

  def _IsInteger(val):
    try:
      int(val)
      return True
    except ValueError:
      return False
    except TypeError:
      return False

  def _ReadProcfs(procfs_entry_pathname):
    try:
      with open(procfs_entry_pathname, 'r') as procfs_entry:
        val = procfs_entry.read().strip()
    except IOError:
      val = None
      sys.stderr('procfs entry not found: %s' % procfs_entry_pathname)
    return val

  for root, directories, unused_files in os.walk(_PROCFS_ROOT):
    # only care about proc info directory. not interested in subdirectories.
    if root != _PROCFS_ROOT:
      continue
    for directory in directories:
      if not _IsInteger(directory):
        continue  # only care about /proc/${PID} directories.
      oom_score_adj = _ReadProcfs(os.path.join(root, directory,
                                               'oom_score_adj'))
      oom_score = _ReadProcfs(os.path.join(root, directory, 'oom_score'))
      # Some cmdline entry contains null chars (e.g. 'screen\0-x\0screenname').
      # It might be nice to put it in a pretty format.
      cmdline = _ReadProcfs(os.path.join(root, directory, 'cmdline'))
      if not oom_score or not oom_score_adj or not cmdline:
        continue  # the process exit()ed?
      procs.append({'pid': directory,
                    'oom_score_adj': oom_score_adj,
                    'oom_score': oom_score,
                    'cmdline': cmdline,
                    })
  return procs


def main():
  if sys.version_info < (2, 7):
    raise 'only tested for 2.7 and up'
  procs = TraverseProcfs()
  for proc in procs:
    print '%s: %s/%s %s' % (proc['pid'],
                            proc['oom_score_adj'],
                            proc['oom_score'],
                            proc['cmdline'])

# TODO(dxy): support short output mode which prints cmdline so that each line
# fits in 80 column instead of a 800-character long command line.

if __name__ == '__main__':
  main()
