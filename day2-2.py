import copy

print('advent of code day 2 part 2')

f = open("input_day2", "r").read()

intcode_original = [int(x) for x in f.split(",")]

#First function (add)
def opcode_one(intcode, n):
    first_position = intcode[n + 1]
    second_position = intcode[n + 2]
    third_position = intcode[n + 3]
    first_num = intcode[first_position]
    second_num = intcode[second_position]
    intcode[third_position] = first_num + second_num
    return intcode

#Second function (multiply)
def opcode_two(intcode, n):
    first_position = intcode[n + 1]
    second_position = intcode[n + 2]
    third_position = intcode[n + 3]
    first_num = intcode[first_position]
    second_num = intcode[second_position]    
    intcode[third_position] = first_num * second_num
    return intcode

#Function to run the Opcode computer
def opcode_computer(intcode):
    n = 0
    while n < len(intcode):
        if intcode[n] == 1:
            opcode_one(intcode, n)
        elif intcode[n] == 2:
            opcode_two(intcode, n)
        elif intcode[n] == 99:
            return intcode
        else:
            print("Error")
        n += 4
    return intcode


#Function to find the noun and the verb of a given output
def find_the_noun_and_verb(coordinate):
    print("Calculating...")
    noun = 0
    while noun < 100:
        verb = 0
        while verb < 100:
            intcode = copy.deepcopy(intcode_original)
            intcode[1] = noun
            intcode[2] = verb
            output = opcode_computer(intcode)
            if output[0] == coordinate:
                print("The noun is %d and the verb is %d for the %d 19690720." % (noun, verb, coordinate))
                return
            verb += 1
        noun += 1

find_the_noun_and_verb(19690720)