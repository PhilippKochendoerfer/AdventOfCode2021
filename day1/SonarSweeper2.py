from SonarSweeper import increment

paths = ["day1_test.txt", "day1.txt"]

for path in paths:
    with open(path) as file:
        lines = file.readlines()

    sums = []
    for i in range(0, len(lines) - 2):
        s = 0;
        for j in range(i, i + 3):
            s += int(lines[j]);
        sums.append(s);

    increment(path, sums)
