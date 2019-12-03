print('advent of code day 1 part 1')

f = open("input", "r")

masses = []

for x in f:
    masses.append(int(x))

print(masses)


def calculate_fuel(mass):
    fuel = (int(mass / 3)) - 2 
    return fuel

print(calculate_fuel(14))

total_fuel = 0
for mass in masses:
    total_fuel += calculate_fuel(mass)
print(total_fuel)

