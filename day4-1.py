print('Advent of Code, Day 4, Part 1')

#Opening the input file
f = open("input_day4", "r").read()

#Creating an interger list with the input file
input = [int(x) for x in f.split("-")]
print(input)

#Creating the 2 variables from our list
start_point = input[0]
end_point = input[1]

#Reassigning those 2 variables for simplicity
a = start_point
b = end_point

#Creating an empty list to store all the possible passwords between a and b meeting all the criterias
passwords = []

#Building a function that will test all the numbers between a and b and keep the possible passwords
#Criterias:
# - Six-digit number: Done!
# - In within the range: Done!
# - Has to have at least 2 adjacent digits that are the same
# - Digits never decrease (they stay the same or increase)

#Range criteria
for x in range(a, b):
    passwords.append(x)

#Six-digits criteria
for password in passwords:
    if len(str(password)) != 6:
        passwords.remove(password)

#At least 2 adjacent digits
breaking_pw_into_digits = [int(x) for x in str(passwords)]

print(breaking_pw_into_digits[1])



print(passwords[10:20])
#And the answer is...: This part was tested with the list input and was working
passwords_count = len(passwords)
print("There is %d different passwords within the range of %d and %d!  Good luck!" % (passwords_count, a, b))
