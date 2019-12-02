"""
Robert Hamby
Dec 2, 2019

Advent of Code, Day 1
Part 1 and 2
https://adventofcode.com/2019/day/1
"""

import math

# The fuel required is the mass divided by three, rounded down and then subtracted by two
def calc_fuel(mass):
	return math.floor(mass / 3) - 2

# Continues to calculate the fuel required until it reaches zero or a negative number
def calc_total(mass):
	current_fuel = calc_fuel(mass)
	total_fuel = current_fuel

	while(True):
		current_fuel = calc_fuel(current_fuel)

		if current_fuel <= 0:
			break
		else:
			total_fuel += current_fuel

	return total_fuel

path = "mass.txt"
mass_arr = []

# Open text file containing masses and adds them to array
with open(path) as f:
	mass_arr = f.read().splitlines()

# Counts and totals fuel calculations
total_fuel = 0;

for mass in mass_arr:
	total_fuel += calc_total(int(mass))

print(str(total_fuel))
