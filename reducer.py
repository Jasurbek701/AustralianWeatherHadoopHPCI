#!/usr/bin/env python3
import sys

current_year = None
max_temp = None
max_temp_details = None
temp_sum = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    year, date, location, temp = line.split('\t', 3)
    temp = float(temp)

    if current_year == year:
        # Accumulate sums and count for average calculation
        temp_sum += temp
        count += 1

        # Check if this temperature is the max for the current year
        if max_temp is None or temp > max_temp:
            max_temp = temp
            max_temp_details = (date, location)
    else:
        # Output for previous year
        if current_year is not None:
            average_temp = temp_sum / count
            max_date, max_location = max_temp_details
            # Only format average_temp with two decimal places
            print(f'{current_year}\t{max_temp}\t{max_date}\t{max_location}\t{average_temp:.2f}')

        # Reset for new year
        current_year = year
        max_temp = temp
        max_temp_details = (date, location)
        temp_sum = temp
        count = 1

# Output for last year
if current_year is not None:
    average_temp = temp_sum / count
    max_date, max_location = max_temp_details
    # Only format average_temp with two decimal places
    print(f'{current_year}\t{max_temp}\t{max_date}\t{max_location}\t{average_temp:.2f}')
