print('advent of code day 2 part 1')

f = open("input_day2", "r").read()

intcode = [int(x) for x in f.split(",")]
#intcode = [1,9,10,3,2,3,11,0,99,30,40,50]
#inccode = [1,0,0,0,99]
#intcode = [2,3,0,3,99]
#intcode = [2,4,4,5,99,0]
#intcode = [1,1,1,4,99,5,6,0,99]


#First function (add)
def opcode_one(n):
    first_position = intcode[n + 1]
    second_position = intcode[n + 2]
    third_position = intcode[n + 3]

    first_num = intcode[first_position]
    second_num = intcode[second_position]

    intcode[third_position] = first_num + second_num

#print(intcode) 

#opcode_one(0)

#print(intcode)

#Second function (multiply)
def opcode_two(n):
    first_position = intcode[n + 1]
    second_position = intcode[n + 2]
    third_position = intcode[n + 3]

    first_num = intcode[first_position]
    second_num = intcode[second_position]

    intcode[third_position] = first_num * second_num

#opcode_two(4)

#print(intcode)

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
            assert "Error"
        n += 4
    return intcode

intcode[1] = 12
intcode[2] = 2

opcode_computer()

print("The value at position zero is %s" % intcode[0])