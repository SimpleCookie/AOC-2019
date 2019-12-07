opCodesReal = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,10,23,27,2,27,13,31,1,31,6,35,2,6,35,39,1,39,5,43,1,6,43,47,2,6,47,51,1,51,5,55,2,55,9,59,1,6,59,63,1,9,63,67,1,67,10,71,2,9,71,75,1,6,75,79,1,5,79,83,2,83,10,87,1,87,5,91,1,91,9,95,1,6,95,99,2,99,10,103,1,103,5,107,2,107,6,111,1,111,5,115,1,9,115,119,2,119,10,123,1,6,123,127,2,13,127,131,1,131,6,135,1,135,10,139,1,13,139,143,1,143,13,147,1,5,147,151,1,151,2,155,1,155,5,0,99,2,0,14,0 ]

opCodes1 = [1,0,0,0,99]
opCodes1_1 = [2,0,0,0,99]

opCodes2 = [2,3,0,3,99]
opCodes2_2 = [2,3,0,6,99]

opCodes3 = [2,4,4,5,99,0]
opCodes3_3 = [2,4,4,5,99,9801]

opCodes4 = [1,1,1,4,99,5,6,0,99]
opCodes4_4 = [30,1,1,4,2,5,6,0,99]

def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

switcher = {
    1: add,
    2: multiply,
}

def runner(opCodes):
    index = 0
    while index < len(opCodes)-1:
        opCode = opCodes[index]

        if (opCode == 99):
            break

        mathFunc = switcher.get(opCode)

        index1 = opCodes[index+1]
        index2 = opCodes[index+2]
        index3 = opCodes[index+3]

        result = mathFunc(opCodes[index1], opCodes[index2])
        opCodes[index3] = result
        index += 4
    return opCodes


print("codes 1: " + str(runner(opCodes1) == opCodes1_1))
print("codes 2: " + str(runner(opCodes2) == opCodes2_2))
print("codes 3: " + str(runner(opCodes3) == opCodes3_3))
print("codes 4: " + str(runner(opCodes4) == opCodes4_4))
print("")
print("")
print("answer: " + str(runner(opCodesReal)[0]))
