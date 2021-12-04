import numpy as numpy

paths = ["day3_test.txt", "day3.txt"]


def main():
    for path in paths:
        with open(path) as file:
            lines = [l.rstrip() for l in file.readlines()]

        print(f"Part1: {path}: {part1(lines)}")

        print(f"Part2: {path}: {part2(lines)}")


def part1(lines):
    input = lines[0].split(",")
    bingo = generateBingo(lines[2:])
    return playBingo(input, bingo)

def part2(lines):
    input = lines[0].split(",")
    bingo = generateBingo(lines[2:])
    return playSquidBingo(input, bingo)


def playBingo(input, games):
    # bingoBool = [[[False] * len(games[0][0])] * len(games[0])] * len(games)
    bingoBool = numpy.full((len(games), len(games[0]), len(games[0][0])), False)

    for number in input:
        for i in range(0, len(games)):
            check = checkNumber(number, games[i])
            if check[0] != -1:
                bingoBool[i][check[0]][check[1]] = True
            if checkBingo(bingoBool[i]):
                return calcPoints(bingoBool[i], games[i], number)
    return -1
    # print(i)
    # printGame(bingoBool)


def playSquidBingo(input, games):
    # bingoBool = [[[False] * len(games[0][0])] * len(games[0])] * len(games)
    bingoBool = numpy.full((len(games), len(games[0]), len(games[0][0])), False)
    playersOut = []
    for number in input:
        for i in range(0, len(games)):
            check = checkNumber(number, games[i])
            if check[0] != -1:
                bingoBool[i][check[0]][check[1]] = True
            if checkBingo(bingoBool[i]):
                if i not in playersOut:
                    playersOut.append(i)
                    if len(playersOut) == len(games):
                        return calcPoints(bingoBool[i], games[i], number)

    return -1
    # print(i)
    # printGame(bingoBool)


def calcPoints(bingoBool, bingo, number):
    sum = 0
    for i in range(0, len(bingoBool)):
        for j in range(0, len(bingoBool)):
            if not bingoBool[i, j]:
                sum += int(bingo[i][j])
    return sum * int(number)


def checkBingo(bingoBool):
    for i in range(0, len(bingoBool)):
        h = True
        v = True
        for j in range(0, len(bingoBool)):
            h = h and bingoBool[i, j]
            v = v and bingoBool[j, i]
        if h or v:
            return True
    return False


def checkNumber(num, bingo):
    for i in range(0, len(bingo)):
        for j in range(0, len(bingo[0])):
            if bingo[i][j] == num:
                return [i, j]
    return [-1, -1]


def generateBingo(lines):
    games = []
    bingo = []
    for row in lines:
        if row != "":
            bingo.append(row.split())
        else:
            games.append(bingo)
            bingo = []
    games.append(bingo)
    return games


def printGame(maxtrix):
    print("")
    for m in maxtrix:
        print("")
        for i in m:
            print(i)
        print("")


if __name__ == "__main__":
    main()
