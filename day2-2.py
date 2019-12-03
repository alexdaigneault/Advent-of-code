import copy

print('advent of code day 2 part 2')

f = open("input_day2", "r").read()

intcode_original = [int(x) for x in f.split(",")]
intcode = copy.deepcopy(intcode_original)

#First function (add)
def opcode_one(n):
    first_position = intcode[n + 1]
    second_position = intcode[n + 2]
    third_position = intcode[n + 3]

    first_num = intcode[first_position]
    second_num = intcode[second_position]

    intcode[third_position] = first_num + second_num

#Second function (multiply)
def opcode_two(n):
    first_position = intcode[n + 1]
    second_position = intcode[n + 2]
    third_position = intcode[n + 3]

    first_num = intcode[first_position]
    second_num = intcode[second_position]

    intcode[third_position] = first_num * second_num

#Function to run the Opcode computer
def opcode_computer():
    n = 0
    while n < len(intcode):
        if intcode[n] == 1:
            opcode_one(n)
        elif intcode[n] == 2:
            opcode_two(n)
        elif intcode[n] == 99:
            return intcode
        else:
            print("Error")
        n += 4
    return intcode


#intcode[1] = 12
#intcode[2] = 2

#opcode_computer()

#print("The value at position zero is %s" % intcode[0])

#Function to find the noun and the verb of a given output
def find_the_noun_and_verb():
    print("Calculating...")
    noun = 0
    while noun < 100:
        verb = 0
        while verb < 100:
            intcode = copy.deepcopy(intcode_original)
            intcode[1] = noun
            intcode[2] = verb
            output = opcode_computer()
            print(output[0])
            if output[0] == 19690720:
                print("The noun is %s and the verb is %s for the coordinate 19690720." % noun, verb)
                print(100 * noun + verb)
                return
            verb += 1
        noun += 1

find_the_noun_and_verb()


