def increment(name, values):
    cnt = 0

    for i in range(0, len(values) - 1):
        if int(values[i + 1]) > int(values[i]):
            cnt += 1

    print(name + ": " + str(cnt))


paths = ["day1_test.txt", "day1.txt"]

for path in paths:
    with open(path) as file:
        lines = file.readlines()

    increment(path, lines)
