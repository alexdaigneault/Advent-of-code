print('advent of code day 1 part 2')

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



def calculate_total_mass(mass):
    total_mass = 0
    calculated_fuel = calculate_fuel(mass)
    while calculated_fuel > 0:
        total_mass += calculated_fuel
        calculated_fuel = calculate_fuel(calculated_fuel)
    return total_mass

print(calculate_total_mass(1969))

total_mass_fuel = 0
for mass in masses:
    total_mass_fuel += calculate_total_mass(mass)
print(total_mass_fuel)