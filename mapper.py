#!/usr/bin/env python3
import sys

# Skip the header row
next(sys.stdin)

for line in sys.stdin:
    # Strip leading and trailing whitespace
    line = line.strip()

    # Split the line into columns
    parts = line.split(',')

    # Skip lines that don't have enough columns
    if len(parts) < 5:
        continue

    date = parts[0]
    location = parts[1]
    temp = parts[3]

    year = date.split('-')[0]

    # Emit year as the key, and a composite value of date, location, and temperature
    print(f'{year}\t{date}\t{location}\t{temp}')
