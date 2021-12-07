paths = ["day7_test.txt", "day7.txt"]


def main():
    for path in paths:
        with open(path) as file:
            lines = [l.rstrip() for l in file.readlines()]
        inp = processInput(lines)

        task2 = [sum([abs(i - j) * (abs(i - j) + 1) / 2 for j in inp]) for i in range(max(inp))]
        task1 = [sum([abs(i - j) for j in inp]) for i in range(max(inp))]

        print(f"Part1: {path}: {min(task1)}")
        print(f"Part2: {path}: {min(task2)}")


def processInput(lines):
    return [int(x) for x in lines[0].split(",")]


if __name__ == "__main__":
    main()
