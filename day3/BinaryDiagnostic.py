paths = ["day3_test.txt", "day3.txt"]


def count(values):
    ones = [0] * (len(values[0]))
    for line in values:
        for index in range(0, len(line)):
            if line[index] == "1":
                ones[index] += 1
    return ones


def gamma(ones, values):
    g = [0] * len(ones)
    length = len(values)
    for i in range(0, len(ones)):
        g[i] = 1 if int(ones[i]) >= length / 2 else 0
    return g


def epsilon(ones, values):
    g = [0] * len(ones)
    length = len(values)
    for i in range(0, len(ones)):
        g[i] = 0 if int(ones[i]) >= length / 2 else 1
    return g


if __name__ == "__main__":
    for path in paths:
        with open(path) as file:
            lines = [l.rstrip() for l in file.readlines()]
        gammaString = "".join([str(i) for i in gamma(count(lines), lines)])
        epsilonString = "".join([str(i) for i in epsilon(count(lines), lines)])

        gammaInt = int(gammaString, 2)
        epsilonInt = int(epsilonString, 2)

        # print(gammaInt)
        # print(epsilonInt)
        # print(gammaInt*epsilonInt)
        print(f"Part 1: {path}: {gammaInt * epsilonInt}")

        filteredGammaLines = lines
        filteredEpsilonLines = lines

        for i in range(0, len(lines[0])):
            gammaArray = gamma(count(filteredGammaLines), filteredGammaLines)
            filteredGammaLines = [j.rstrip() for j in filteredGammaLines if gammaArray[i] == int(j[i])]
            if len(filteredGammaLines) <= 1:
                break
        for i in range(0, len(lines[0])):
            epsilonArray = epsilon(count(filteredEpsilonLines), filteredEpsilonLines)
            filteredEpsilonLines = [j.rstrip() for j in filteredEpsilonLines if epsilonArray[i] == int(j[i])]
            if len(filteredEpsilonLines) <= 1:
                break

        # print(int(filteredGammaLines[0], 2))
        # print(int(filteredEpsilonLines[0], 2))

        print(f"Part 2: {path}: {int(filteredGammaLines[0], 2) * int(filteredEpsilonLines[0], 2)}")

        # print(filteredGammaLines)
        # print(filteredEpsilonLines)
