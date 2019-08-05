# -*- coding: utf-8 -*-

import re

months = {}
for line in open("months.txt"):
    parts = line.split()
    months[parts[1].lower()] = parts[2]

weekdays = {}

for line in open("weekdays.txt"):
    parts = line.split()
    weekdays[parts[0].lower()] = parts[2]

regex = re.compile("^(\d+)\. ?([^ ]+)(?: \(([^)]*)\))?.*\n$")

for line in open("dates.txt"):
    matches = regex.match(line)

    if matches:
        date, month, day = matches.groups()

        if day:
            print "%s %s %s" % (weekdays[day], date, months[month])
        else:
            print "%s %s" % (date, months[month])


