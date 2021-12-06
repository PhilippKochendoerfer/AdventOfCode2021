paths = ["day6_test.txt", "day6.txt"]


def main():
    for path in paths:
        with open(path) as file:
            lines = [l.rstrip() for l in file.readlines()]
        print(f"Part1: {path}: {sum(simulateEfficient(processInput(lines), 80))}")
        print(f"Part2: {path}: {sum(simulateEfficient(processInput(lines), 256))}")


def processInput(lines):
    return [int(x) for x in lines[0].split(",")]


def simulateEfficient(fishes, days):
    fishCounter = [0] * 9

    for fish in fishes:
        fishCounter[fish] += 1
    for day in range(1, days + 1):
        #print(day)
        newFish = fishCounter[0]
        for i in range(0, 8):
            fishCounter[i] = fishCounter[i + 1]
        fishCounter[8] = newFish
        fishCounter[6] += newFish
        #print(sum(fishCounter))
    return fishCounter


def simulate(fishes, days):
    # print(f"Initial state: {fishes}")
    for day in range(1, days + 1):
        #print(day)
        for i in range(0, len(fishes)):

            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1
        # print(f"After {day} day: {fishes}")
    return fishes


if __name__ == "__main__":
    main()
