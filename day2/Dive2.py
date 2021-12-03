paths = ["day2_test.txt", "day2.txt"]
for path in paths:
    with open(path) as file:
        lines = file.readlines()
    pos = [0, 0]
    aim = 0
    for line in lines:
        command = line.split(" ")
        match command[0]:
            case "forward":
                pos[0] += int(command[1])
                pos[1] += int(command[1]) * aim
            case "down":
                aim += int(command[1])
            case "up":
                aim -= int(command[1])

    print(path+": "+str(pos[0] * pos[1]))
