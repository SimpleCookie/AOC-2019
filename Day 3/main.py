from copy import deepcopy
import concurrent.futures

testCords1 = {
    1: ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
    2: ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
    "answer": 159
}
testCords2 = {
    1: ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
    2: ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
    "answer": 135
}

def intersection(list1, list2):
    return [value for value in list1 if value in list2]

def getNextCords(prev, pos):
    direction = pos[0:1]
    steps = int(pos[1:])
    nextSteps = []
    if (direction == "U"):
        for i in range(1, steps + 1):
            tmpPrev = deepcopy(prev)
            tmpPrev["y"] += i
            nextSteps.append(tmpPrev)
    elif (direction == "R"):
        for i in range(1, steps + 1):
            tmpPrev = deepcopy(prev)
            tmpPrev["x"] += i
            nextSteps.append(tmpPrev)
    elif (direction == "D"):
        for i in range(1, steps + 1):
            tmpPrev = deepcopy(prev)
            tmpPrev["y"] -= i
            nextSteps.append(tmpPrev)
    elif (direction == "L"):
        for i in range(1, steps + 1):
            tmpPrev = deepcopy(prev)
            tmpPrev["x"] -= i
            nextSteps.append(tmpPrev)
    return nextSteps

def convertCords(input):
    cords = [{ "x": 0, "y": 0 }]
    for pos in input:
        nextCords = getNextCords(cords[-1], pos)
        for nextCord in nextCords:
            cords.append(nextCord)
    return cords

def getMinDistance(input):
    return min(map(lambda cord: abs(cord["x"]) + abs(cord["y"]), input))

def compute(input):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(convertCords, input[1])
        future2 = executor.submit(convertCords, input[2])
        cords1 = future1.result()
        cords2 = future2.result()
        intersections = intersection(cords1, cords2)

        return getMinDistance(intersections[1:])

testAnswer1 = compute(testCords1)
testAnswer2 = compute(testCords2)
print("test1: " + str(testAnswer1 == testCords1["answer"]) + " got: " + str(testAnswer1))
print("test1: " + str(testAnswer2 == testCords2["answer"]) + " got: " + str(testAnswer2))

with open("Day 3/data.txt") as _file:
    realCords = {
        1: [cord for cord in _file.readline().split(",")],
        2: [cord for cord in _file.readline().split(",")]
    }
    answerPart1 = compute(realCords)
    print("real: " + str(answerPart1))
    # Answer is 266
