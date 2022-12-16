#!/usr/bin/env python

with open('/Users/eraldahoxha/Documents/learning/adventofcode/inputs/day1.txt') as f:
    lines = f.readlines()
calories = 0
maxCalories = 0


for line in lines: 
    if line != "\n":
        calories += int(line)
        if calories > maxCalories:
            maxCalories = calories  
    else:
        calories = 0
        continue
print(maxCalories)
