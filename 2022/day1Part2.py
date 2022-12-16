#!/usr/bin/env python

with open('/Users/eraldahoxha/Documents/learning/adventofcode/inputs/day1.txt') as f:
    lines = f.readlines()
calories = 0
total = 0
list = []

for line in lines: 
    if line != "\n":
        calories += int(line)
        list.append(calories)
    else:
        calories = 0
        continue
ld = sorted(list, reverse=True)
total = sum(ld[:3]) 
print(total)
