#/bin/bash

# show the most recent commands that match the pattern. with no pattern,
# just show the most recent.  care is taken to eliminate this command or
# its relatives = and r.

history | sed 's/^ *[0-9][0-9]* *//; /^ *[=hr]$/d; /^ *[hr=] /d; ' | \
egrep " *"$@ | uniq | tail

