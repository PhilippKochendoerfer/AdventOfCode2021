import numpy

paths = ["day5_test.txt", "day5.txt"]


def main():
    for path in paths:
        with open(path) as file:
            lines = [l.rstrip() for l in file.readlines()]

        ocean = part1(lines)
        print(f"Part1: {path}: {countVents(ocean)}")
        ocean = part2(lines, ocean)
        print(f"Part2: {path}: {countVents(ocean)}")


def calcMax(segments):
    maximum = 0
    for segment in segments:
        for pos in segment:
            for value in pos:
                if int(value) > maximum:
                    maximum = int(value)
    return maximum


def part1(lines):
    segments = getVerticalAndHorizontal(lines)
    maxValue = calcMax(segments)
    ocean = numpy.zeros((maxValue + 1, maxValue + 1))
    for segment in segments:
        for i in range(min(int(segment[0][0]), int(segment[1][0])), max(int(segment[0][0]), int(segment[1][0])) + 1):
            for j in range(min(int(segment[0][1]), int(segment[1][1])),
                           max(int(segment[0][1]), int(segment[1][1])) + 1):
                ocean[i][j] += 1
    return ocean


def countVents(ocean):
    cnt = 0
    for line in ocean:
        for field in line:
            if field >= 2:
                cnt += 1
    return cnt


def part2(lines, ocean):
    segments = getDiagonal(lines)

    for segment in segments:
        x = int(segment[0][0])
        y = int(segment[0][1])

        ocean[x][y] += 1
        while (True):
            x += numpy.sign(int(segment[1][0]) - int(segment[0][0]))
            y += numpy.sign(int(segment[1][1]) - int(segment[0][1]))
            ocean[x][y] += 1
            if x == int(segment[1][0]):
                break
    return ocean


def getDiagonal(lines):
    segments = []
    for line in lines:
        entry = line.split(" -> ")
        x = []
        for pos in entry:
            coord = pos.split(",")
            x.append(coord)
        if (abs(int(x[0][0]) - int(x[1][0]))) == (abs(int(x[0][1]) - int(x[1][1]))):
            segments.append(x)
    return segments


def getVerticalAndHorizontal(lines):
    segments = []
    for line in lines:
        entry = line.split(" -> ")
        x = []
        for pos in entry:
            coord = pos.split(",")
            x.append(coord)
        if (x[0][0] == x[1][0]) or (x[0][1] == x[1][1]):
            segments.append(x)
    return segments


if __name__ == "__main__":
    main()
